from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .config import default_config_path, load_config, save_config
from .models import AuthorConfig
from .sync import print_status, run_sync


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="x-archive",
        description="本地归档 X 博主帖子（默认通过 Nitter RSS，无需 X API）",
    )
    parser.add_argument("--version", action="version", version=f"x-archive {__version__}")

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--config",
        "-c",
        default=str(default_config_path()),
        help="配置文件路径（默认: ./config.json）",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    p_sync = sub.add_parser("sync", parents=[common], help="拉取并增量保存配置中的博主")
    p_sync.add_argument(
        "--handle",
        action="append",
        default=None,
        help="只同步指定 handle，可重复传入；默认同步全部",
    )
    p_sync.set_defaults(func=cmd_sync)

    p_status = sub.add_parser("status", parents=[common], help="查看本地归档与同步状态")
    p_status.set_defaults(func=cmd_status)

    p_add = sub.add_parser("add", parents=[common], help="添加一个博主到配置")
    p_add.add_argument("handle", help="博主 handle，如 naval")
    p_add.add_argument("--note", default="", help="备注，如「创业/哲学」")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", parents=[common], help="列出配置中的博主")
    p_list.set_defaults(func=cmd_list)

    p_init = sub.add_parser("init", parents=[common], help="创建用户配置（默认 ~/.ky-x）")
    p_init.set_defaults(func=cmd_init)

    return parser


def cmd_sync(args: argparse.Namespace) -> int:
    results = run_sync(args.config, only_handles=args.handle)
    ok = 0
    fail = 0
    new_total = 0
    for r in results:
        if r.error:
            fail += 1
            print(f"✗ @{r.handle}: {r.error}")
        else:
            ok += 1
            new_total += r.new
            print(
                f"✓ @{r.handle}: 拉取 {r.fetched}，新增 {r.new}，过滤 {r.skipped_filter}"
            )
    print("")
    print(f"完成: 成功 {ok}，失败 {fail}，新增合计 {new_total}")
    try:
        cfg = load_config(args.config)
        print(f"归档位置: {Path(cfg.output_dir).expanduser().resolve()}")
    except Exception:
        pass
    return 1 if fail and not ok else 0


def cmd_status(args: argparse.Namespace) -> int:
    print_status(args.config)
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    cfg = load_config(args.config)
    handle = args.handle.lstrip("@").strip().lower()
    existing = {a.normalized_handle() for a in cfg.authors}
    if handle in existing:
        print(f"@{handle} 已在配置中")
        return 0
    cfg.authors.append(AuthorConfig(handle=handle, note=args.note or ""))
    path = save_config(cfg, args.config)
    print(f"已添加 @{handle} → {path}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    cfg = load_config(args.config)
    for a in cfg.authors:
        note = f" — {a.note}" if a.note else ""
        print(f"@{a.normalized_handle()}{note}")
    return 0


def cmd_init(args: argparse.Namespace) -> int:
    target = Path(args.config).expanduser()
    if target.exists():
        print(f"配置已存在: {target}")
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    data_dir = (Path.home() / ".ky-x" / "data").resolve()
    payload = {
        "output_dir": str(data_dir),
        "source": "nitter_rss",
        "nitter_instances": ["https://nitter.net"],
        "request_timeout_sec": 25,
        "request_delay_sec": 1.0,
        "filters": {
            "include_replies": False,
            "include_retweets": False,
            "include_quotes": True,
        },
        "authors": [
            {"handle": "naval", "note": "示例：改成你要跟的博主"}
        ],
    }
    example = Path(__file__).resolve().parent.parent / "config.example.json"
    if example.exists():
        import json as _json

        try:
            raw = _json.loads(example.read_text(encoding="utf-8"))
            raw["output_dir"] = str(data_dir)
            payload = raw
        except Exception:
            pass
    import json as _json

    target.write_text(
        _json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"已创建配置: {target}")
    print(f"默认归档目录: {data_dir}")
    print("添加博主: python3 -m xarchive add <handle> -c", target)
    print("开始同步: python3 -m xarchive sync -c", target)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(f"错误: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

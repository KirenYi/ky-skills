#!/usr/bin/env python3
"""Generate a simple designed .icns for Codex 切换模型 (stdlib only)."""
from __future__ import annotations

import math
import struct
import subprocess
import tempfile
import zlib
from pathlib import Path


def png_chunk(tag: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + tag
        + data
        + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    )


def write_png(path: Path, w: int, h: int, rgba: bytes) -> None:
    raw = b""
    stride = w * 4
    for y in range(h):
        raw += b"\x00" + rgba[y * stride : (y + 1) * stride]
    compressed = zlib.compress(raw, 9)
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)
    data = b"\x89PNG\r\n\x1a\n" + png_chunk(b"IHDR", ihdr) + png_chunk(b"IDAT", compressed) + png_chunk(b"IEND", b"")
    path.write_bytes(data)


def lerp(a, b, t):
    return int(a + (b - a) * t)


def pixel(x, y, n):
    # coords -1..1
    cx = (x + 0.5) / n * 2 - 1
    cy = (y + 0.5) / n * 2 - 1
    r = math.hypot(cx, cy)
    # rounded square-ish soft circle icon
    if r > 0.98:
        return (0, 0, 0, 0)
    # soft edge
    edge = 1.0
    if r > 0.90:
        edge = max(0.0, (0.98 - r) / 0.08)
    # background gradient indigo -> violet
    t = (cy + 1) / 2
    br, bg, bb = lerp(30, 88, t), lerp(34, 80, t), lerp(64, 200, t)
    # inner glow
    g = max(0.0, 1 - r * 1.15)
    br = min(255, int(br + 40 * g))
    bg = min(255, int(bg + 30 * g))
    bb = min(255, int(bb + 50 * g))
    # white "swap" arcs (two curved chevrons suggesting switch)
    a = 255
    # ring
    if 0.62 < r < 0.72:
        br, bg, bb = 255, 255, 255
        a = int(230 * edge)
        return (br, bg, bb, a)
    # top arrow head
    if -0.15 < cy < 0.05 and 0.15 < cx < 0.45 and abs(cy + 0.05 - (cx - 0.3) * 0.4) < 0.08:
        return (255, 255, 255, int(240 * edge))
    if -0.35 < cy < -0.05 and 0.05 < cx < 0.35 and abs(cy + 0.2 + (cx - 0.2) * 0.5) < 0.07:
        return (255, 255, 255, int(240 * edge))
    # bottom arrow
    if -0.05 < cy < 0.15 and -0.45 < cx < -0.15 and abs(cy - 0.05 + (cx + 0.3) * 0.4) < 0.08:
        return (255, 255, 255, int(240 * edge))
    if 0.05 < cy < 0.35 and -0.35 < cx < -0.05 and abs(cy - 0.2 - (cx + 0.2) * 0.5) < 0.07:
        return (255, 255, 255, int(240 * edge))
    # accent dot
    if math.hypot(cx - 0.0, cy - 0.0) < 0.12:
        return (180, 220, 255, int(255 * edge))
    return (br, bg, bb, int(255 * edge))


def render(n: int) -> bytes:
    buf = bytearray(n * n * 4)
    for y in range(n):
        for x in range(n):
            r, g, b, a = pixel(x, y, n)
            i = (y * n + x) * 4
            buf[i : i + 4] = bytes((r, g, b, a))
    return bytes(buf)


def build_icns(out_icns: Path) -> None:
    sizes = [16, 32, 64, 128, 256, 512, 1024]
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        iconset = td / "AppIcon.iconset"
        iconset.mkdir()
        for s in sizes:
            rgba = render(s)
            png = td / f"{s}.png"
            write_png(png, s, s, rgba)
            # standard iconset names
            if s == 16:
                names = ["icon_16x16.png"]
            elif s == 32:
                names = ["diana.k@example.org", "icon_32x32.png"]
            elif s == 64:
                names = ["ivan.p@example.net"]
            elif s == 128:
                names = ["icon_128x128.png"]
            elif s == 256:
                names = ["wendy.h@example.net", "icon_256x256.png"]
            elif s == 512:
                names = ["wendy.h@example.net", "icon_512x512.png"]
            else:
                names = ["walt.e@example.net"]
            for name in names:
                (iconset / name).write_bytes(png.read_bytes())
        out_icns.parent.mkdir(parents=True, exist_ok=True)
        subprocess.check_call(["iconutil", "-c", "icns", str(iconset), "-o", str(out_icns)])
        # also keep a 512 png preview
        preview = out_icns.with_suffix(".png")
        write_png(preview, 512, 512, render(512))
        print(f"wrote {out_icns}")
        print(f"wrote {preview}")


if __name__ == "__main__":
    root = Path(__file__).resolve().parent / "assets"
    build_icns(root / "CodexSwitch.icns")

# How it works

## Profiles

`codex-provider` rewrites a managed block at the top of `~/.codex/config.toml`:

```toml
model = "..."
model_provider = "..."   # omitted for official OpenAI/ChatGPT auth
model_catalog_json = "..."  # SuperGrok catalog only
```

Providers are registered once under `[model_providers.*]`.

## Channels

| Profile group | Transport |
|---------------|-----------|
| openai | Codex built-in ChatGPT / API auth |
| grok | Local proxy `127.0.0.1:18765` → `cli-chat-proxy.grok.com` with SuperGrok OAuth |
| claude*, deepseek*, gemini | `https://openrouter.ai/api/v1` + `OPENROUTER_API_KEY`, `wire_api=responses` |

## Why not direct DeepSeek / Anthropic URLs?

Current Codex only speaks the **Responses** wire API. Many vendor “OpenAI-compatible” endpoints only implement Chat Completions. OpenRouter (and similar gateways) expose Responses-compatible routes for third-party models.

## Extending

Edit `~/.codex/ky-profiles.json` (or skill `scripts/profiles.json` then reinstall):

1. Add a profile with `model`, `model_provider`, `requires_env`
2. Ensure `providers` has the matching provider block
3. `codex-provider use <new-id>`

## Desktop apps

`make-desktop-apps.sh` builds LSUIElement apps that call `codex-provider-app-run <id|pick>`.

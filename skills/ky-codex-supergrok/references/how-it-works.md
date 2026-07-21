# How it works

## Two different “Grok” paths

| Path | Auth | Billing | Endpoint |
|------|------|---------|----------|
| **SuperGrok (this skill)** | `grok login` → `~/.grok/auth.json` OAuth | Subscription quota | `https://cli-chat-proxy.grok.com` |
| Paid API | `XAI_API_KEY` | Per-token at console.x.ai | `https://api.x.ai/v1` |

This skill implements the **subscription** path only.

## Components

1. **`supergrok-token`**  
   Reads / refreshes the OAuth access token from `~/.grok/auth.json` via `auth.x.ai`.

2. **`supergrok-proxy`** (default `127.0.0.1:18765`)  
   - Adds headers required by the CLI chat proxy (`X-XAI-Token-Auth`, `x-grok-client-version`, …)  
   - Adapts Codex Responses bodies that SuperGrok rejects (e.g. `additional_tools`)  
   - Optionally rewrites “based on GPT-5” developer text  
   - By default does **not** use macOS system HTTP proxy (avoids CONNECT 503 through local VPN ports)

3. **`codex-provider`**  
   Rewrites a managed block at the top of `~/.codex/config.toml` and can restart ChatGPT/Codex Desktop.

4. **Desktop apps**  
   Thin launchers calling `codex-provider-app-run` → `codex-provider`.

## Codex config (after install)

```toml
[model_providers.xai]
name = "xAI SuperGrok"
base_url = "http://127.0.0.1:18765/v1"
wire_api = "responses"

# When Grok mode is active (managed by codex-provider):
model = "grok-4.5"
model_provider = "xai"
model_catalog_json = "~/.codex/model-catalogs/xai-models.json"
```

## Why the model may still say “GPT-5”

Codex injects long developer instructions that start with “You are Codex, an agent based on GPT-5…”.  
The proxy rewrites many of these strings, but UI / residual prompts can still confuse self-identification.  
Trust **provider name + proxy logs**, not chat self-description.

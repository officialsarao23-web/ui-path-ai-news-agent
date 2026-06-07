# UiPath AI News Agent 🤖

A UiPath Coded Agent built with **LangGraph** that fetches daily AI news from Tavily, summarizes with Groq, and sends it to Telegram — scheduled to run automatically at **8 AM IST**.

## Architecture

```
START → fetch_news → summarize → format → send_telegram → END
```

| Node | Tool | Purpose |
|---|---|---|
| `fetch_news` | **Tavily Search API** | Searches "artificial intelligence AI news today", returns top 5 articles |
| `summarize` | **Groq llama-3.3-70b-versatile** | Writes 2-sentence plain-English summaries for each article |
| `format` | — | Builds a rich Telegram message with emojis, summaries, and links |
| `send_telegram` | **Telegram Bot API** | Posts the formatted message to your Telegram chat |

## Project Structure

```
├── src/
│   ├── main.py                     # LangGraph StateGraph wiring
│   └── nodes/
│       ├── fetch_news.py           # Tavily search node
│       ├── summarize.py            # Groq LLM summarization node
│       ├── format.py               # Message formatting node
│       └── send_telegram.py        # Telegram sender node
├── pyproject.toml                  # Python dependencies
├── uipath.json                     # UiPath project config
├── langgraph.json                  # LangGraph config
├── bindings.json                   # Orchestrator Asset bindings
└── entry-points.json               # Auto-generated entry point schema
```

## Prerequisites

### Orchestrator Assets (create before first run)

Create these **String** assets in Orchestrator → Assets:

| Name | Description |
|---|---|
| `TAVILY_API_KEY` | API key from [tavily.com](https://tavily.com) |
| `GROQ_API_KEY` | API key from [console.groq.com](https://console.groq.com) |
| `TELEGRAM_BOT_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | Your Telegram chat ID |

## Local Development

```bash
.venv\Scripts\activate
pip install -r requirements.txt    # or use pyproject.toml
uip codedagent setup --force
uip codedagent init
uip codedagent run graph '{"trigger": "daily"}'
```

## Deploy

```bash
uip codedagent pack
uip codedagent publish --my-workspace
```

## Schedule (Orchestrator)

1. Go to **Processes** → `my-uipath-agent` → **Triggers** → **Add Trigger**
2. Set:
   - **Type:** Schedule
   - **Timezone:** `(UTC+05:30) India Standard Time`
   - **Frequency:** Daily — **Time:** `08:00`
   - **Process:** `my-uipath-agent`
   - **Alert:** "Generate alert if job started and not completed" (timeout: 15 min)

## Tech Stack

- **LangGraph** — State graph orchestration
- **UiPath Python SDK** — Orchestrator Asset retrieval
- **Tavily** — AI news search
- **Groq** — LLM summarization (llama-3.3-70b)
- **Telegram Bot API** — Message delivery

from datetime import date

NUMBER_EMOJIS = ["1\uFE0F\u20E3", "2\uFE0F\u20E3", "3\uFE0F\u20E3", "4\uFE0F\u20E3", "5\uFE0F\u20E3"]


def format_node(state):
    today = date.today().isoformat()
    lines = [f"\U0001F916 Daily AI News \u2014 {today}", "\u2501" * 26]
    for i, s in enumerate(state.summaries):
        emoji = NUMBER_EMOJIS[i] if i < len(NUMBER_EMOJIS) else f"{i + 1}."
        lines.append(f"{emoji} {s['title']}")
        lines.append(f"\U0001F4CC {s['summary']}")
        lines.append(f"\U0001F517 {s['url']}")
        lines.append("")
    lines.append("\u2501" * 26)
    lines.append("Powered by your AI News Agent \U0001F680")
    return {"message": "\n".join(lines)}

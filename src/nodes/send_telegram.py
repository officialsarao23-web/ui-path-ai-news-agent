from uipath.platform import UiPath
import requests


def _get_asset(name: str) -> str:
    sdk = UiPath()
    asset = sdk.assets.retrieve(name)
    return asset.value


def send_telegram_node(state):
    token = _get_asset("TELEGRAM_BOT_TOKEN")
    chat_id = _get_asset("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": state.message,
        "disable_web_page_preview": True,
    }
    resp = requests.post(url, json=payload)
    if resp.status_code == 200:
        print("Telegram message sent successfully")
        return {"status": "success"}
    msg = f"Failed to send Telegram message: {resp.status_code} {resp.text}"
    print(msg)
    raise RuntimeError(msg)

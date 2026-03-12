import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_audio(file_path: str, caption: str = "오늘의 아침 금융 브리핑입니다."):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {
            "chat_id": CHAT_ID,
            "caption": caption
        }
        response = requests.post(url, data=data, files=files, timeout=60)

    response.raise_for_status()
    print("텔레그램 전송 완료")
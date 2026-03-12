from news import get_news
from summary import summarize_news
from market import get_market_data
from voice import text_to_speech
from telegram_send import send_telegram_audio


def main():
    print("시장 데이터 수집 시작...")
    market = get_market_data()
    print("시장 데이터 수집 완료")

    print("뉴스 수집 시작...")
    news = get_news()
    print("뉴스 수집 완료")

    print("GPT 요약 시작...")
    briefing_text = summarize_news({
        "market": market,
        "news": news
    })
    print("GPT 요약 완료")

    print(briefing_text)

    print("음성 생성 시작...")
    text_to_speech(briefing_text)
    print("음성 생성 완료")

    print("텔레그램 전송 시작...")
    send_telegram_audio("morning_briefing.mp3")
    print("텔레그램 전송 완료")


if __name__ == "__main__":
    main()
from news import get_news
from summary import summarize_news
from voice import text_to_speech
from market import get_market_data


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

 #   print("음성 생성 시작...")
 #   text_to_speech(briefing_text)
 #  print("음성 생성 완료")


if __name__ == "__main__":
    main()
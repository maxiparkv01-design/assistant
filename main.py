from news import get_news
from summary import summarize_news
from voice import text_to_speech


def main():
    news = get_news()

    briefing_text = summarize_news(news)

    print(briefing_text)

    text_to_speech(briefing_text)


if __name__ == "__main__":
    main()
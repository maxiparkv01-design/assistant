from news import get_news
from briefing import make_briefing
from voice import text_to_speech


def main():

    news = get_news()

    briefing_text = make_briefing(news)

    print(briefing_text)

    text_to_speech(briefing_text)


if __name__ == "__main__":
    main()
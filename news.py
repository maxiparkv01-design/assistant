import re
import requests
import feedparser

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

URLS = {
    "AI": "https://news.google.com/rss/search?q=AI&hl=ko&gl=KR&ceid=KR:ko",
    "경제": "https://news.google.com/rss/search?q=경제&hl=ko&gl=KR&ceid=KR:ko",
    "금융": "https://news.google.com/rss/search?q=금융&hl=ko&gl=KR&ceid=KR:ko",
    "증시": "https://news.google.com/rss/search?q=증시&hl=ko&gl=KR&ceid=KR:ko",
}

STOPWORDS = {
    "있다", "없다", "되다", "한다", "위한", "대한", "관련", "현장",
    "정부", "한국", "오늘", "내일", "기자", "단독", "속보", "칼럼",
    "설명자료", "주간", "일정", "장중", "마감", "발언", "논의",
    "기자", "기사", "강해", "항복", "패배", "선언"
}


def clean_title(title: str) -> str:
    title = title.strip()
    if " - " in title:
        title = title.rsplit(" - ", 1)[0].strip()
    return title


def extract_keywords(title: str) -> set[str]:
    text = clean_title(title)
    words = re.findall(r"[가-힣A-Za-z0-9]+", text)

    keywords = set()
    for word in words:
        word = word.lower()
        if len(word) <= 1:
            continue
        if word in STOPWORDS:
            continue
        keywords.add(word)

    return keywords


def is_similar_title(title: str, selected_titles: list[str]) -> bool:
    current_keywords = extract_keywords(title)

    for selected in selected_titles:
        selected_keywords = extract_keywords(selected)
        overlap = current_keywords & selected_keywords

        # 핵심 단어가 2개 이상 겹치면 같은 이슈로 간주
        if len(overlap) >= 2:
            return True

    return False


def get_news(limit_per_category: int = 3) -> dict[str, list[str]]:
    results = {}

    for category, url in URLS.items():
        titles = []

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            feed = feedparser.parse(response.text)

            for entry in feed.entries:
                title = clean_title(entry.title)

                if not title:
                    continue

                if is_similar_title(title, titles):
                    continue

                titles.append(title)

                if len(titles) >= limit_per_category:
                    break

        except Exception as e:
            print(f"{category} 뉴스 수집 오류: {e}")

        results[category] = titles

    return results
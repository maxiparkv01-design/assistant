import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_news(news: dict[str, list[str]]) -> str:
    prompt = f"""
아래 뉴스 제목들을 바탕으로 한국어 아침 뉴스 브리핑을 작성해줘.

조건:
- 카테고리별로 구분해줘: AI, 경제, 금융, 증시
- 각 카테고리는 1~2문장으로 짧게 요약해줘
- 제목을 그대로 나열하지 말고, 공통 흐름을 자연스럽게 정리해줘
- 과장 없이 담백한 뉴스 앵커 톤으로 써줘
- 전체 분량은 1분 내외로 읽을 수 있게 짧게 작성해줘
- 마지막에 "이상 오늘의 아침 뉴스 브리핑이었습니다."를 넣어줘

뉴스 데이터:
{news}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "너는 한국어 아침 뉴스 브리핑 작성자다."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        max_tokens=400,
    )

    return response.choices[0].message.content.strip()
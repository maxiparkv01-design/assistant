import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_news(news: dict[str, list[str]]) -> str:
    prompt = f"""
다음 금융시장 데이터와 뉴스 제목을 기반으로 아침 금융 브리핑을 작성해줘.

구성:
1. 금융시장 브리핑
   - USD/KRW
   - USD/JPY
   - BTC / ETH / SOL
   - Gold / WTI
   - S&P500 / NASDAQ100
   - KOSPI / KOSDAQ

2. 주요 뉴스 요약

조건:
- 한국어 뉴스 앵커 톤
- 1분 내외 브리핑
- 숫자와 등락률을 자연스럽게 설명
- 금융시장 분위기를 한두 문장으로 정리
- 마지막 문장은 반드시
"이상 오늘의 아침 금융 브리핑이었습니다."로 끝낼 것

데이터:
{news}
"""

    try:
        print("GPT 요약 요청 시작...")

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "너는 한국어 아침 뉴스 브리핑 작성자다."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
            max_tokens=1000,
        )

        print("GPT 요약 응답 완료")
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("GPT 호출 오류:", e)
        return "GPT 요약 중 오류가 발생했습니다."
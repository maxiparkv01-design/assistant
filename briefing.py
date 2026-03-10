def make_briefing(news: dict[str, list[str]]) -> str:
    lines = []
    lines.append("좋은 아침입니다. 오늘의 뉴스 브리핑입니다.")
    lines.append("")

    for category, titles in news.items():
        if not titles:
            continue

        lines.append(f"{category} 뉴스입니다.")

        for title in titles:
            lines.append(f"- {title}")

        lines.append("")

    lines.append("이상 오늘의 아침 뉴스 브리핑이었습니다.")
    return "\n".join(lines)
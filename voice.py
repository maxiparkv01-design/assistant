from gtts import gTTS


def text_to_speech(text):

    tts = gTTS(text=text, lang="ko")

    tts.save("morning_briefing.mp3")

    print("음성 파일 생성 완료: morning_briefing.mp3")
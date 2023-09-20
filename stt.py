import speech_recognition as sr
from gtts import gTTS

def convert_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something:")
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        error_feed="Could not understand audio"
        print(error_feed)
        tts = gTTS(text=error_feed, lang='en')
        tts.save('error.mp3')
        return None
    except sr.RequestError as e:
        error_feed="Could not request results; {0}".format(e)
        print(error_feed)
        tts = gTTS(text=error_feed, lang='en')
        tts.save('error.mp3')
        return None

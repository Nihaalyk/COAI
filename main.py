import speech_recognition as sr
from model import chatmodel
from gtts import gTTS
import os

def convert_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something:")
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        print(user_input)
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
    

def main():
    while True:
        user_input = convert_speech_to_text()
        if user_input:
            # Call the chat model function to get the response
            response_text = chatmodel(user_input)

            # Print the conversation
            print("User:", user_input)
            print("Bot:", response_text)

            # Convert bot response to audio
            tts = gTTS(text=response_text, lang='en')
            tts.save('response.mp3')
            os.system('cvlc response.mp3')  # Use any suitable audio player


if __name__ == "__main__":
    main()

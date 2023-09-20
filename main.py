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
        return user_input
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
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
            os.system('mpg123 response.mp3')  # Use any suitable audio player

if __name__ == "__main__":
    main()

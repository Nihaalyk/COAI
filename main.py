from stt import convert_speech_to_text
from model import chatmodel
from speak import speak

import time 

def main():
    while True:
        user_input = convert_speech_to_text()
        if user_input:
            # Call the chat model function to get the response
            response_text = chatmodel(user_input)

            # Print the conversation
            print("User:", user_input)
            print("Bot:", response_text)

            speak(response_text)
            time.sleep(1)

if __name__ == "__main__":
    main()

from stt import convert_speech_to_text
from model import chatmodel
import pyaudio
from gtts import gTTS
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

            # Convert bot response to audio
            tts = gTTS(text=response_text, lang='en')
            tts.save('response.mp3')

            # Play the audio using PyAudio
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(2),
                            channels=1,
                            rate=44100,
                            output=True)
            with open('response.mp3', 'rb') as f:
                audio_data = f.read()
            stream.write(audio_data)
            stream.stop_stream()
            stream.close()
            p.terminate()

            time.sleep(1)

if __name__ == "__main__":
    main()

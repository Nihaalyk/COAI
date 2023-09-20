import pyaudio
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='en')
    audio = tts.get_wav_data()

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)
    stream.write(audio)
    stream.stop_stream()
    stream.close()
    p.terminate()
from gtts import gTTS
import pygame
import os

def speak(text):
    # Create a gTTS object and save it as an audio file
    tts = gTTS(text=text, lang='en')
    filename = 'speech.mp3'
    tts.save(filename)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(filename)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Stop mixer and cleanup
    pygame.mixer.quit()

    # Remove the temporary audio file
    os.remove(filename)
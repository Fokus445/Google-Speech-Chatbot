
import os
import random
import string
import time

import pygame
from google.cloud import texttospeech


class GoogleTextToSpeech():

    def __init__(self, language_code: str):
        # init tts_client
        self.tts_client = texttospeech.TextToSpeechClient()
        self.language_code = language_code

    def speak(self, text):
        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code=self.language_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = self.tts_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        fname = os.getcwd() + '/tts-temp' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)) + '.mp3'

        # The response's audio_content is binary.
        out = open(fname, 'wb')
        # Write the response to the output file.
        out.write(response.audio_content)
        #print('Audio content written to file ' + fname)
        out.close()

        pygame.mixer.init()
        pygame.mixer.music.load(fname)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        pygame.mixer.quit()
        os.remove(fname)


   

if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "/service-key.json"
    LANGUAGE_CODE = "en-US" #lt-LT
    test = GoogleTextToSpeech(LANGUAGE_CODE)
    test.speak("Testing Google Text To Audio API and Pygame audio player")
import pyttsx3
import speech_recognition as sr

from ._base import ITranscriber


class AudioTranscriber(ITranscriber):
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recogniser = sr.Recognizer()

    def transcribe(self, file: str) -> str:
        with sr.AudioFile(file) as audio:
            clip = self.recogniser.record(audio)

        try:
            return self.recogniser.recognize_google(clip)

        except:
            print("Could not recognise audio")

    def vocalise(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()

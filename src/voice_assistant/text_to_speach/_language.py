import pyttsx3
import speech_recognition as sr

from ._base import ILanguageModule


class AudioTranscriber(ILanguageModule):
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recogniser = sr.Recognizer()

    def run(self, file: str) -> str:
        with sr.AudioFile(file) as audio:
            clip = self.recogniser.record(audio)

        try:
            return self.recogniser.recognize_google(clip)

        except:
            print("Could not recognise audio")


class TextVocaliser(ILanguageModule):
    def __init__(self):
        self.engine = pyttsx3.init()

    def vocalise(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()

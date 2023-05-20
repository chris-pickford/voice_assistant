import pyttsx3
import speech_recognition as sr

from ._base import ITranscriber


class AudioTranscriber(ITranscriber):
    def __init__(self):
        self.recogniser = sr.Recognizer()

    def transcribe(self, file: str) -> str:
        pass

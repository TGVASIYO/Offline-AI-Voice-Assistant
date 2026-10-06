"""
Speech-to-Text Module
Uses Faster-Whisper for offline speech recognition.
"""

from faster_whisper import WhisperModel


class SpeechToText:
    """
    Converts speech (audio file) into text.
    """

    def __init__(self):

        print("Loading Whisper Model...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper Model Loaded Successfully!")

    def transcribe(self, audio_path):

        print("\nConverting Speech to Text...")

        segments, info = self.model.transcribe(audio_path)

        text = ""

        for segment in segments:
            text += segment.text + " "

        return text.strip()
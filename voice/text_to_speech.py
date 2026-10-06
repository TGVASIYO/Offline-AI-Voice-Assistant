"""
Offline Text-to-Speech Module
Uses Piper TTS
Author: Team AURA
"""

import os
import subprocess
import tempfile
from playsound import playsound


class TextToSpeech:
    def __init__(self):
        # Project root folder
        base_dir = os.path.dirname(os.path.dirname(__file__))

        # Piper executable
        self.piper_exe = os.path.join(
            base_dir,
            "tts",
            "piper",
            "piper.exe"
        )

        # Voice model
        self.voice_model = os.path.join(
            base_dir,
            "tts",
            "voice",
            "en_US-lessac-medium.onnx"
        )

        print("\n========== TTS DEBUG ==========")
        print("Piper EXE :", self.piper_exe)
        print("Voice Model :", self.voice_model)
        print("Piper Exists :", os.path.exists(self.piper_exe))
        print("Voice Exists :", os.path.exists(self.voice_model))
        print("================================\n")

    def speak(self, text):

        if not text.strip():
            print("No text to speak.")
            return

        # Temporary output file
        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_audio:
            output_file = temp_audio.name

        command = [
            self.piper_exe,
            "--model",
            self.voice_model,
            "--output_file",
            output_file
        ]

        print("Generating speech...")

        result = subprocess.run(
            command,
            input=text,
            text=True,
            capture_output=True
        )

        print("\n===== PIPER OUTPUT =====")
        print("Return Code :", result.returncode)
        print("STDOUT :")
        print(result.stdout)
        print("STDERR :")
        print(result.stderr)
        print("========================\n")

        if os.path.exists(output_file):
            print("Playing audio...")
            playsound(output_file)
            os.remove(output_file)
        else:
            print("ERROR: Output audio file was not created.")
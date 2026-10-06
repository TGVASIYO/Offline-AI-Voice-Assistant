import openwakeword
from openwakeword.model import Model
import pyaudio
import numpy as np


class WakeWordDetector:

    def __init__(self):
        # Download/load the default OpenWakeWord models
        openwakeword.utils.download_models()

        self.model = Model(
            wakeword_models=["hey_jarvis"]
        )

        self.audio = pyaudio.PyAudio()

        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=1280
        )

    def wait_for_wake_word(self):

        print("\nAURA is sleeping...")
        print("Say: Hey Jarvis")

        while True:

            audio_data = self.stream.read(
                1280,
                exception_on_overflow=False
            )

            audio_array = np.frombuffer(
                audio_data,
                dtype=np.int16
            )

            prediction = self.model.predict(audio_array)

            for wake_word, score in prediction.items():

                if score > 0.5:
                    print("\nWake word detected!")
                    return True
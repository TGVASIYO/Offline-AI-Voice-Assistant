"""
Microphone Recorder Module
Author: Team AURA
"""

import os
import time
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

from voice.config import (
    SAMPLE_RATE,
    CHANNELS,
    DTYPE,
    AUDIO_FOLDER,
    AUDIO_FILE
)


# ==========================
# Silence Detection Settings
# ==========================

SILENCE_DURATION = 2.0       # Stop after 2 seconds of silence
SILENCE_THRESHOLD = 500      # Lower = more sensitive to quiet sounds
MAX_RECORD_SECONDS = 15      # Safety limit


class AudioRecorder:
    """
    Records audio from the microphone and automatically
    stops when the user is silent for 2 seconds.
    """

    def __init__(self):
        os.makedirs(AUDIO_FOLDER, exist_ok=True)

    def record(self):

        print("=" * 60)
        print("🎤 Recording Started...")
        print("Speak now...")
        print("⏹️ Recording will stop after 2 seconds of silence.")
        print("=" * 60)

        chunk_duration = 0.1
        chunk_size = int(SAMPLE_RATE * chunk_duration)

        audio_chunks = []

        silence_time = 0
        speech_started = False
        start_time = time.time()

        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=DTYPE,
            blocksize=chunk_size
        ) as stream:

            while True:

                # Read microphone audio
                audio_chunk, overflowed = stream.read(chunk_size)

                # Save this audio chunk
                audio_chunks.append(audio_chunk.copy())

                # Convert audio to numpy array
                audio_data = audio_chunk.astype(np.float32)

                # Calculate volume (RMS)
                volume = np.sqrt(np.mean(audio_data ** 2))

                # Check whether user is speaking
                if volume > SILENCE_THRESHOLD:

                    speech_started = True
                    silence_time = 0

                else:

                    # Only count silence after speech has started
                    if speech_started:
                        silence_time += chunk_duration

                # Stop after 2 seconds of silence
                if speech_started and silence_time >= SILENCE_DURATION:

                    print("\n⏹️ 2 seconds of silence detected.")
                    break

                # Safety timeout
                if time.time() - start_time >= MAX_RECORD_SECONDS:

                    print("\n⏹️ Maximum recording time reached.")
                    break

        # Combine all recorded chunks
        recording = np.concatenate(audio_chunks, axis=0)

        # Save WAV file
        write(
            AUDIO_FILE,
            SAMPLE_RATE,
            recording
        )

        print("✅ Recording Finished")
        print(f"Saved to: {AUDIO_FILE}")

        return AUDIO_FILE
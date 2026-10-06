"""
Configuration settings for the Voice Module.
"""

# ==========================
# Audio Configuration
# ==========================

# Sample rate (Whisper works best with 16 kHz audio)
SAMPLE_RATE = 16000

# Mono recording (1 channel)
CHANNELS = 1

# Audio format
DTYPE = "int16"

# Recording duration (seconds)
RECORD_SECONDS = 5

# Audio folder and filename
AUDIO_FOLDER = "audio"
AUDIO_FILE = f"{AUDIO_FOLDER}/input.wav"
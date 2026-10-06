from voice.recorder import AudioRecorder
from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech
from voice.wake_word import WakeWordDetector


def main():

    # Create objects
    wake_word = WakeWordDetector()
    recorder = AudioRecorder()
    stt = SpeechToText()
    tts = TextToSpeech()

    while True:

        # Wait for wake word
        wake_word.wait_for_wake_word()

        print("\n🎙️ AURA is listening...")

        # Record user's command
        audio_path = recorder.record()

        # Convert speech to text
        text = stt.transcribe(audio_path)

        print("\nRecognized Text:")
        print(text)

        # Speak response
        tts.speak(text)


if __name__ == "__main__":
    main()
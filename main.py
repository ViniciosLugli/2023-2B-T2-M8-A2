import numpy as np
import simpleaudio as sa
from txtai.pipeline import TextToSpeech


class VoiceSynthesizer:  # Handles the text-to-speech conversion using a specified model.
    def __init__(self, model_name):
        self.tts = TextToSpeech(model_name)  # Initializes the TextToSpeech pipeline with a given model.

    def synthesize(self, text):
        return self.tts(text)  # Converts text to audio using the specified text-to-speech model.


class AudioPlayer:  # Provides functionality to play audio data.
    @staticmethod
    def play_audio(audio_data, sample_rate):
        audio = np.int16(audio_data * 32767).tobytes()  # Converts audio data to 16-bit PCM format.
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)  # Plays the audio buffer.
        play_obj.wait_done()  # Waits for the audio playback to complete.


class VoiceSynthApp:  # Combines the VoiceSynthesizer and AudioPlayer to create a text-to-speech application.
    def __init__(self, synthesizer, audio_player):
        self.synthesizer = synthesizer  # Instance of the VoiceSynthesizer class.
        self.audio_player = audio_player  # Instance of the AudioPlayer class.

    def run(self):
        while True:
            text = input("Enter a phrase to synthesize, type 'exit' to leave: ")  # Prompt user for text input.
            if text.lower() == 'exit':
                break  # Exits the loop if the user types 'exit'.
            audio = self.synthesizer.synthesize(text)  # Synthesizes the entered text to audio.
            self.audio_player.play_audio(audio, 22050)  # Plays the synthesized audio.


# Main execution block: Initializes and runs the application.
if __name__ == "__main__":
    synthesizer = VoiceSynthesizer("NeuML/ljspeech-jets-onnx")  # Creates a VoiceSynthesizer instance with a specific model.
    audio_player = AudioPlayer()  # Creates an AudioPlayer instance.
    app = VoiceSynthApp(synthesizer, audio_player)  # Initializes the application with the synthesizer and audio player.
    app.run()  # Runs the application.

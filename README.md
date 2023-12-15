# Voice Synth Application

This quick start provides instructions for setting up and using the Voice Synth Application, a python based text-to-speech tool, it uses a combination of `numpy`, `simpleaudio`, and `txtai` to synthesize and play text as audio, the application is ideal for experimenting with voice synthesis in Python.

## Requirements

Before you start, ensure you have all necessary dependencies installed.

### Setting up a Virtual Environment

It's recommended to use a virtual environment to manage the dependencies. Here's how you can set it up:

```bash
# Install virtualenv if not already installed
pip install virtualenv

# Create a virtual environment in the project directory
python -m venv venv
```

To activate the virtual environment, run:

```bash
# On Windows
venv\Scripts\activate.bat

# On Linux or macOS
source venv/bin/activate
```

### Installing Dependencies

Once the virtual environment is active, install the dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include `numpy`, `simpleaudio`, and `txtai`.

## Configuration

No additional configuration is required for this application. The voice synthesizer model (`NeuML/ljspeech-jets-onnx`) is hardcoded in the application.

## Usage

To use the Voice Synth Application, follow these steps:

1. Start the application by running:

    ```bash
    python main.py
    ```

2. Once the application is running, you will be prompted to enter a phrase to synthesize. Type your desired text and press Enter.

3. The application will synthesize the entered text into speech and play it through your default audio output device.

4. To exit the application, type 'exit' when prompted for text input.

### Main Components

-   **VoiceSynthesizer**: This class handles the text-to-speech conversion using the specified `txtai` model.
-   **AudioPlayer**: A utility class to play the synthesized audio.
-   **VoiceSynthApp**: The main application class combining the synthesizer and audio player functionalities.

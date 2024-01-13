# Morse Code Converter

## Overview

This project is a Morse code converter implemented in Python. It provides functionalities to convert speech to Morse code, text to Morse code, Morse code to text, and Morse code to speech. The program utilizes the SpeechRecognition library for speech-to-text conversion, the pyttsx3 library for text-to-speech conversion, and the playsound library for playing Morse code audio.

## Features

- **Speech to Morse Code:** Converts spoken words to Morse code.
- **Text to Morse Code:** Converts a given text to Morse code.
- **Morse Code to Text:** Converts Morse code to plain text.
- **Morse Code to Speech:** Converts Morse code to speech.

## Dependencies

Make sure to install the required libraries before running the program:
```bash
pip install SpeechRecognition pyttsx3 playsound
```

## Usage
1. **Clone the Repository:**
   ```bash
    git clone https://github.com/Antisource/MorseCodeConvertor.git
   ```

2. **Run the Program:**
   ```bash
    python main.py
   ```
   OR
   ```bash
   main.exe
   ```

You will be prompted to choose an option:

- **1** for Speech to Morse Code
- **2** for Text to Morse Code
- **3** for Morse to Speech
- **4** for Morse to Text
- Follow the instructions for the selected option.

## Morse Code Dictionary

The program uses the following Morse code dictionary for conversion:

```python
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
                   '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'}
```

## Audio Files

The program uses two audio files, short.mp3 for a short Morse code signal and long.mp3 for a long Morse code signal. Make sure these files are present in the same directory as the script.

## Note

- Ensure your microphone is connected and properly configured for speech-to-text functionality.
- Adjust the volume levels for a better experience with Morse code audio.

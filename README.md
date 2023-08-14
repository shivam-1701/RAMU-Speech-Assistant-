<h1 align="center">Ramu - Your Voice Assistant</h1>

## Overview

Ramu is a simple voice assistant script written in Python. It listens for voice commands and performs various tasks based on the commands received.

## Features

- Play YouTube videos
- Provide the current time
- Fetch information from Wikipedia
- Tell jokes
- Open applications like Spotify, Photoshop, Premiere Pro, etc.
- Send WhatsApp messages
- And more...

## Prerequisites

Before running the script, make sure you have the required Python packages installed:

```bash
pip install speech_recognition pyttsx3 pywhatkit wikipedia pyjokes deepspeech webbrowser
```
How to Use
Clone this repository:
```
git clone https://github.com/your-username/ramu-voice-assistant.git
cd ramu-voice-assistant
```
Run the script:
```
python ramu.py
```
Start giving voice commands to Ramu and see it in action!
Usage Example
Here's an example of how you can use Ramu in your Python script:
```
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time
import pyjokes
import os
import deepspeech
import subprocess
import webbrowser
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# ... (rest of your code)

while True:
    run_ramu()
```
Feel free to customize and enhance Ramu's capabilities by adding more commands and functionalities.

Contributions are welcome! If you find any issues or want to add new features, feel free to create a pull request.

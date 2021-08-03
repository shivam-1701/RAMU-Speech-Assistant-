import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time
import pywhatkit as kit
import pyjokes
import os
import deepspeech
import subprocess
import webbrowser
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
engine. setProperty("rate", 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ramu' in command:
                command = command.replace('ramu', '')
                print(command)

    except:
        pass
    return command


def run_ramu():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'how are you' in command:
        talk('I am really good thank you!')
    elif 'bajao' in command:
        song = command.replace('bajao', '')
        talk('baja rha hu.... ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'samay' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('samay ho raha hai ' + time)
    elif 'tell me something about' in command:
        person = command.replace('tell me something about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'tell me a knock knock joke' in command:
        talk('knock knock')
    elif 'who is there' in command:
        talk('Lettuce')
    elif 'lettuce who' in command:
        talk('Lettuce in, it is cold out here.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'let us chess' in command:
        pywhatkit.search("chess.com")
        chess = command.replace('let us chess', '')
        talk('lets play chess ' + chess)
    elif 'google' in command:
        pywhatkit.search(command)
        google = command.replace('google', '')
        talk('searching ' + google)
    elif 'what is' in command:
        pywhatkit.search(command)
        google = command.replace('what is', '')
        talk('searching ' + google)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'music' in command:
        music_dir = 'C:\\Users\\Pradeep Pandey\\Music\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        talk('playing music for you')
    elif 'send whatsapp message' in command:
        kit.sendwhatmsg("+91 7303212884", "Hello",16,54)
    elif 'alexa' in command:
        talk('I am better than her hahaha')
    elif 'bixby' in command:
        talk('I am better than him hahaha')
    elif 'siri' in command:
        talk('I am better than her hahaha')
    elif 'open spotify' in command:
        talk('opening spotify')
    elif 'open photoshop' in command:
        subprocess.Popen('C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe')
        talk('opening photoshop')
    elif 'open premiere pro' in command:
        subprocess.Popen('C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe')
        talk('opening premiere pro')
    elif 'open candy crush' in command:
        talk('opening candy crush')
    elif 'open netflix' in command:
        talk('opening netflix')
    elif 'open spotify' in command:
        talk('opening spotify')
    elif 'open android studio' in command:
        subprocess.Popen('C:\\Program Files\\Android\\Android Studio\\bin\\launcher.exe')
        talk('opening android studio')
    elif 'open spotify' in command:
        subprocess.Popen('C:\\Users\\Pradeep Pandey\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\spotify.exe')
        talk('opening spotify')
    elif 'goodbye' in command:
        talk("Cheers")
        sys.exit("Goodbye")
    else:
        talk('Please say the command again.')

while True:
    run_ramu()

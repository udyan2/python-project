from datetime import date
import os
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import playsound
import datetime
import subprocess
import wikipedia
import smtplib
import webbrowser as wb
import time

def speak(text):
    tts = gTTS(text = text, lang="en-UK")
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
def gudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as lk:
            print("Exception: "+str(lk))
    return said.lower()
text = gudio()

if 'remind me' in text:
    speak('starting reminder')
    import time
    print("What shall I remind you about?")
    speak("What shall I remind you about?")
    king = str(input())
    print("In how many minutes?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    print(king)
    speak(king)

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
import sys, webbrowser
import pyttsx3
import record
eng = pyttsx3.init()
voice_in=record.recorder()


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

def open_maps(): 
    if len(sys.argv) > 1:
        eng.say('opening maps') 
        eng.runAndWait()
        input(map_string)
        map_string = ''.join(sys.argv[1:]) 
        webbrowser.open('https://www.google.com/maps/place/' + map_string) 
      
    else: 
        print ("Pass the string as command line argument, Try Again")
        eng.say(“Failed. Try Again”)
        eng.runAndWait()


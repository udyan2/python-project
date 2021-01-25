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
import pyttsx3
import record
eng = pyttsx3.init()
voice_in = record.recorder()

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

def youtube_():
    eng.say("What should I search?")
    eng.runAndWait()
    voice_in = voice_in.replace("open youtube and search","")
    Search_term = text
    eng.say("Here we go to Youtube\n")
    eng.runAndWait
    wb.open("https://www.youtube.com/results?search_query=" + Search_term)
    
def youtube_music():
    voice_in = voice_in.replace('play the song',"")
    Search_term = text
    eng.say("Here we go to Youtube Music\n")
    eng.runAndWait()
    wb.open("https://music.youtube.com/search?q=" + Search_term)
    
def stop_listen():
    eng.say("for how much minutes you want me to stop listening commands")
    eng.runAndWait()
    a = gudio()
    time.sleep(int(a))
    print(a)

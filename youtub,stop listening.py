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

if 'open youtube and search' in text:
    speak("What should I search?")
    text = text.replace("open youtube and search","")
    Search_term = text
    speak("Here we go to Youtube\n")
    wb.open("https://www.youtube.com/results?search_query=" + Search_term)
    
if 'play the song' in text:
    text = text.replace('play the song',"")
    Search_term = text
    speak("Here we go to Youtube Music\n")
    wb.open("https://music.youtube.com/search?q=" + Search_term)
    
if "don't listen" in text or "stop listening" in text:
    speak("for how much minutes you want me to stop listening commands")
    a = gudio()
    time.sleep(int(a))
    print(a)
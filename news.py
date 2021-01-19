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
import requests
from urllib.request import urlopen
import json

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




if 'news' in text:    
    try:
        

        jsonObj = urlopen('''http://newsapi.org/v2/everything?q=bitcoin&from=2020-12-18&sortBy=publishedAt&apiKey=4b982e554dd9425989b47ba5ad21a6c4''')
        data = json.load(jsonObj)
        i = 1
                
        speak('here are some top news from the times of india')
        print('''=============== TOP HEADLINES ============'''+ '\n')
                
        for item in data['articles']:
            
                    
            print(str(i) + '. ' + item['title'] + '\n')
            print(item['description'] + '\n')
            speak(str(i) + '. ' + item['title'] + '\n')
            i += 1
                    
    except Exception as e:
            
            print(str(e))

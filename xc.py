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
import psutil #pip
import pyjokes

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
        except Exception as e:
            print("Exception: "+str(e))
    return said.lower()
text = gudio()
if 'hello' in text:
    speak("Hi, How are you?")
if 'what is the time' in text:
    def time_():
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        speak("The current time is")
        speak(Time)
    time_()
if 'search on wikipedia about' in text:
    speak("Searching.....")
    text = text.replace('search on wikipedia about','')
    result = wikipedia.summary(text,sentences = 2)
    speak('According to Wikipedia')
    print(result)
    speak(result)
if 'send an email' in text:
    def sendinganemail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        ## need low security for email.

        server.login('suryawolfgaming@gmail.com','passsword')
        server.close()
    try:
        speak("Whome should i send it to?")
        reciever = input('Email of reciever:')
        speak("what should i say?")
        content = gudio()
        to = reciever
        sendinganemail(to,content)
        speak(content)
        speak('Email has been sent')
    except Exception as e:
        print(e)
        speak('Unable to send email')  
if "cpu" in text:
    def cpuusage():
        usage = str(psutil.cpu_percent())
        speak('CPU is at'+usage)
        battery = psutil.sensors_battery()
        speak ('battery is at')
        speak(str(battery.percent()))
    cpuusage()
if "battery" in text:
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(str(battery.percent()))
if "tell me a joke" in text:
    def joke():
        speak(pyjokes.get_joke())
        print(pyjokes.get_joke())
    joke()
if "Sleep" in text:
    speak("Going Offline")
    quit()
if 'word' in text:
    speak("Opening Word....")
    msworld = r"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
    os.startfile(msworld)
if 'excel' in text:
    speak("Opening Excel.....")
    msexcel = r"C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"
    os.startfile(msexcel)
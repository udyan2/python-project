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
if 'search' in text:
    speak("What to search?")
    chromepath = "C:\ProgramFiles\Google\Chrome\Application\chrome.exe %s"
    #location of chrome
    search = gudio()
    wb.get(chromepath).open_new_tab(search+'.com')

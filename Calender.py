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

if "what is the date today" in text:
    
    today = date.today()

# dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print(d1)
    speak(d1)

    if d1 == "01/01/2021":            
        print("Happy New Year")
        speak("Happy New Year")

    elif d1 == "13/01/2021":
        print("Happy Lohri")
        speak("Happy Lohri")
    
    elif d1 == "14/01/2021":
        
        print("Happy Makar Sakranti")
        speak("Happy Makar Sakranti")
    
    elif d1 == "20/01/2021":
        print("Guru Gobind Singh Jayanti")
        speak("Guru Gobind Singh Jayanti")
    
    elif d1 == "26/01/2021":
        print("Happy Republic Day")
        speak("Happy Republic Day")
    
    elif d1 == "16/02/2021":
        print("Vasant Panchami")
        speak("Vasant Panchami")

    elif d1 == "11/03/2021":
        print("Maha-Shivratari")
        speak("Maha-Shivratari")
    
    elif d1 == "29/03/2021":
        print("Happy Holi")
        speak("Happy Holi")
    
    elif d1 == "02/04/2021":
        print("A very happy Good Friay to You")
        speak("A very happy Good Friay to You")
    
    elif d1 == "04/04/2021":
        print("Wishing YOu a Very Happy Easter Day")
        speak("Wishing YOu a Very Happy Easter Day")
    
    elif d1 == "21/04/2021":
        print("Happy Ram-Navmi")
        speak("Happy Ram-Navmi")
    
    elif d1 == "25/04/2021":
        print("Happy Mahavir Jayanti")
        speak("Happy Mahavir Jayanti")
    
    elif d1 == "13/05/2021":
        print("May Allah Shower his mercy on this Ramdan upon you and your family")
        speak("May Allah Shower his mercy on this Ramdan upon you and your family")
    
    elif d1 == "20/07/2021":
        print("Wishing You a blessed Bakar-id")
        speak("Wishing You a blessed Bakar-id")
    
    elif d1 == "15/08/2021":
        print("Happy  Independence Day")
        speak("Happy  Independence Day")

    elif d1 == "19/08/2021":
        print("Happy Muharram")
        speak("Happy Muharram")
        
    elif d1 == "21/08/2021":
        print("Happy Onam")
        speak("Happy Onam")
    
    elif d1 == "22/08/2021":
        print("Sending you loads of Love and Greetings, Happy Raksha Bandhan")
        speak("Sending you loads of Love and Greetings, Happy Raksha Bandhan")
    
    elif d1 == "30/08/2021":
        print("May all Your Prayers be answered, Happy Janamashtami")
        speak("May all Your Prayers be answered, Happy Janamashtami")
    
    elif d1 == "10/09/2021":
        print("May god Ganesha bless you and your family with Lots of wisdom and fortune, Happy Ganesh Chaturthi")
        speak("May god Ganesha bless you and your family with Lots of wisdom and fortune, Happy Ganesh Chaturthi")
    
    elif d1 == "02/10/2021":
        print("Happy Mahatama Gandhi Jayanti")
        speak("Happy Mahatama Gandhi Jayanti")
    
    elif d1 == "15/10/2021":
        print("May This Dussehra bring lots of light and Happiness in your life")
        speak("May This Dussehra bring lots of light and Happiness in your life")
    
    elif d1 == "04/11/2021":
        print("May God Light up your future, Happy Diwali")
        speak("May God Light up your future, Happy Diwali")
    
    elif d1 == "25/12/2021":
        print("Merry Christmas")
        speak("Merry Christmas")
    
    elif d1 == "31/12/2021":
        print("I hope you Party Hard and Enjoy yourself today, Gear up for the new Year's Eve")
        speak("I hope you Party Hard and Enjoy yourself today, Gear up for the new Year's Eve")
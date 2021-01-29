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

from chatterbot import ChatBot

# naming the ChatBot calculator
# using mathematical evaluation logic
# the calculator AI will not learn with the user input
Bot = ChatBot(name = 'Calculator',
                read_only = True,                  
                logic_adapters = ["chatterbot.logic.MathematicalEvaluation"],                 
                storage_adapter = "chatterbot.storage.SQLStorageAdapter")
    

# clear the screen and start the calculator
print('\033c')
eng.say("Hello, I am a calculator. How may I help you?")
eng.runAndWait()
print("Hello, I am a calculator. How may I help you?")
while (True):
    # take the input from the user
    user_input = input("me: ")
    
    # check if the user has typed quit to exit the prgram   
    if user_input.lower() == 'quit':
        eng.say("Exiting")
        eng.runAndWait()
        print("Exiting")
        break

    # otherwise, evaluate the user input
    # print invalid input if the AI is unable to comprehend the input
    try:
        response = Bot.get_response(user_input)
        print("Calculator:", response)
    except:
        print("Calculator: Please enter valid input.")
        eng.say("Calculator: Please enter valid input")
        eng.runAndWait()
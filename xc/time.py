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
import pyautogui
import pywhatkit
import pyttsx3
import record
eng = pyttsx3.init()
voice_in=record.recorder()
def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    eng.say("The current time is")
    eng.runAndWait()
    eng.say(Time)
    eng.runAndWait()
time_()
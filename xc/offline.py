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
eng = pyttsx3.init()
def byebye():
    eng.say("Going Offline")
    eng.runAndWait()
    quit()
byebye()
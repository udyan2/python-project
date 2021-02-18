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
def word_():
    eng.say("Opening Word....")
    eng.runAndWait()
    msworld = r"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
    os.startfile(msworld)
word_()
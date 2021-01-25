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
def vscode():
    eng.say("Opening VSCode....")
    eng.runAndWait()
    Vscode = r"C:/Users/LENOVO/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    os.startfile(Vscode)
vscode()
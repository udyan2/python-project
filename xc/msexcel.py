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
def excel_():
    eng.say("Opening Excel.....")
    eng.runAndWait()
    msexcel = r"C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"
    os.startfile(msexcel)
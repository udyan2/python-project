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
voice_in = record.recorder()
def note(voice_in):
    file_name = "samplenote.txt"
    with open(file_name,"w") as f:
        f.write(voice_in)
    subprocess.Popen(["notepad.exe", file_name])
eng.say("what should I write")
eng.runAndWait()
note_voice_in = voice_in()
note(note_voice_in)
eng.say("done")

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
eng.say("What should I remember?")
eng.runAndWait()
memo = voice_in()
eng.say("You asked me to remember"+memo)
eng.runAndWait()
rem = open('memo.txt','w')
rem.write(memo)
rem.close()
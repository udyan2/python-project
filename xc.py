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
def wikipedia_():
    eng.say("Searching.....")
    eng.runAndWait()
    voice_in = voice_in.replace('search on wikipedia about','')
    result = wikipedia.summary(voice_in,sentences = 2)
    eng.say('According to Wikipedia')
    eng.runAndWait()
    print(result)
    eng.say(result)
    eng.runAndWait()
def sendinganemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    ## need low security for email.

    server.login('suryawolfgaming@gmail.com','passsword')
    server.close()
try:
    eng.say("Whome should i send it to?")
    eng.runAndWait()
    reciever = input('Email of reciever:')
    eng.say("what should i say?")
    eng.runAndWait()
    content = voice_in()
    to = reciever
    sendinganemail(to,content)
    eng.say(content)
    eng.runAndWait()
    eng.say('Email has been sent')
    eng.runAndWait()
except Exception as e:
    print(e)
    eng.say('Unable to send email')  
    eng.runAndWait()

def cpuusage():
    usage = str(psutil.cpu_percent())
    eng.say('CPU is at'+usage)
    eng.runAndWait()
def battery_():
    battery = psutil.sensors_battery()
    eng.say('Battery is at')
    eng.runAndWait()
    eng.say(battery.percent)
    eng.runAndWait()
def joke():
    joke = pyjokes.get_joke()
    eng.say(joke)
    eng.runAndWait
    print(joke)
def byebye():
    eng.say("Going Offline")
    eng.runAndWait()
    quit()
def word_():
    eng.say("Opening Word....")
    eng.runAndWait()
    msworld = r"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
    os.startfile(msworld)
def excel_():
    eng.say("Opening Excel.....")
    eng.runAndWait()
    msexcel = r"C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"
    os.startfile(msexcel)## what should i search
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
def vscode():
    eng.say("Opening VSCode....")
    eng.runAndWait()
    Vscode = r"C:/Users/LENOVO/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    os.startfile(Vscode)
def screenshot():
    img = pyautogui.screenshot()
    img.save('F:/screenshot.png')
    eng.say("Done.........")
    eng.runAndWait()
########### Whatsapp message at a particular time##################
if "play" in voice_in:
    eng.say("To which number")
    eng.runAndWait()
    whatnum = voice_in()
    eng.say("what is the message?")
    eng.runAndWait()
    whatmessage = voice_in()
    eng.say("At what Hour?")
    eng.runAndWait()
    whatHour = voice_in()
    eng.say("At what Min?")
    eng.runAndWait()
    whatmin = voice_in()
    whatHour1 = eval(whatHour)
    whatmin1 = eval(whatmin)
    pywhatkit.sendwhatmsg('+91{}',format(whatnum),whatmessage,whatHour1,whatmin1)
    '7589423463'
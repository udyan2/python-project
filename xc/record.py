# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:42:42 2021

@author: Udyan Sharma
"""
import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
eng = pyttsx3.init()

def recorder():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_in=''
        try:
            voice_in=r.recognize_google(audio)
            print(voice_in)
        except sr.UnknownValueError:
            print( '' )
            eng.say("Sorry, I did not get that.")
            eng.runAndWait()
        except sr.WaitTimeoutError:
            eng.say("Wait timeout error.")
            eng.runAndWait()
        except sr.RequestError:
            eng.say("Sorry, the service is currently down.")
            eng.runAndWait()
        return voice_in
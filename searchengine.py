    # -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 00:10:07 2021

@author: Udyan Sharma
"""
import webbrowser
import pyttsx3
import record

def searchm():
    eng = pyttsx3.init()
    l=['search in google','search in bing','search in yahoo']
    eng.say("Entered search module")
    eng.say("Which Search Engine Should I Open?")
    eng.runAndWait()
    voice_in=record.recorder()
    for el in l:
        if el in voice_in.lower():
            seng=el[10:len(el)+1]+'.com'
            #webbrowser.open_new(eng)
            # Windows
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(seng)
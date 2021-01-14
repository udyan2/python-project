# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 00:10:07 2021

@author: Udyan Sharma
"""
import webbrowser


def searchm():
    l=['search in google','search in bing','search in yahoo']
    eng.say("Entered search module")
    eng.runandWait()
    voice_in=recorder()
    text='search in yahoo'
    for el in l:
        if el in text:
            eng=el[10:len(el)+1]+'.com'
            #webbrowser.open_new(eng)
            # Windows
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(eng)
import webbrowser as wb
from os import path
import pyttsx3
import record
import wikipedia

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[0].id)

def searchm():
    l=['search in google','search in bing','search in yahoo']
    lex=['search in wikipedia','search in youtube']
    eng.say("Entered search module")
    eng.say("Where should I search?")
    eng.runAndWait()
    voice_in=record.recorder()
    if voice_in.lower() in l:
        el=voice_in.lower()
        seng=el[10:len(el)+1]+'.com'
        #webbrowser.open_new(eng)
        # Windows
        eng.say("What should I search?")
        eng.runAndWait()
        sterm=record.recorder()
        chrome_path1 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        chrome_path2 = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        if(path.exists(chrome_path1)):
            chrome_path=chrome_path1
            print("Chrome path 1")
        else:
            chrome_path=chrome_path2
            print("Chrome path 2")
        wb.get(chrome_path).open(seng + '/search?q=' + sterm)
        return 1
    elif voice_in.lower() in lex:
        if 'search in youtube' in voice_in.lower():
            eng.say("What should I search?")
            eng.runAndWait()
            sterm=record.recorder()
            wb.open("https://www.youtube.com/results?search_query=" + sterm)
        if 'search in wikipedia' in voice_in.lower():
            eng.say("What do you want to search about?")
            eng.runAndWait()
            sterm=record.recorder()
            eng.say("Searching.....")
            eng.runAndWait()
            result = wikipedia.summary(sterm,sentences = 2)
            eng.say('According to Wikipedia')
            eng.runAndWait()
            print(result)
            eng.say(result)
            eng.runAndWait()
        return 1
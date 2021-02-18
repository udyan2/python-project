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
    print("Xceleron: Where should I search?")
    eng.say("Where should I search?")
    eng.runAndWait()
    voice_in=record.recorder()
    if voice_in.lower() in l:
        el=voice_in.lower()
        seng=el[10:len(el)+1]+'.com'
        #webbrowser.open_new(eng)
        # Windows
        print("Xceleron: What should I search?")
        eng.say("What should I search?")
        eng.runAndWait()
        sterm=record.recorder()
        chrome_path1 = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        chrome_path2 = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        if(path.exists(chrome_path1)):
            chrome_path=chrome_path1
            print("Xceleron: Using Google Chrome path 1 (32 bit)")
        else:
            chrome_path=chrome_path2
            print("Xceleron: Using Google Chrome path 2 (64 bit)")
        wb.get(chrome_path).open(seng + '/search?q=' + sterm)
        return 1
    elif voice_in.lower() in lex:
        if 'search in youtube' in voice_in.lower():
            print("Xceleron: What should I search?")
            eng.say("What should I search?")
            eng.runAndWait()
            sterm=record.recorder()
            wb.open("https://www.youtube.com/results?search_query=" + sterm)
        if 'search in wikipedia' in voice_in.lower():
            print("Xceleron: What do you want to search about?")
            eng.say("What do you want to search about?")
            eng.runAndWait()
            sterm=record.recorder()
            print("Xceleron: Searching...")
            eng.say("Searching...")
            eng.runAndWait()
            result = wikipedia.summary(sterm,sentences = 2)
            print("Xceleron: According to Wikipedia:")
            eng.say('According to Wikipedia')
            eng.runAndWait()
            print("Xceleron:",result)
            eng.say(result)
            eng.runAndWait()
        check=1
        return check
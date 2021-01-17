import webbrowser as wb
import pyttsx3
import record

def searchm():
    eng = pyttsx3.init()
    l=['search in google','search in bing','search in yahoo']
    eng.say("Entered search module")
    eng.say("Where should I search?")
    eng.runAndWait()
    voice_in=record.recorder()
    for el in l:
        if el in voice_in.lower():
            seng=el[10:len(el)+1]+'.com'
            #webbrowser.open_new(eng)
            # Windows
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chrome_path).open(seng + '/search?q=' + sterm)
    if 'search in youtube' in voice_in.lower():
            eng.say("What should I search?")
            eng.runAndWait()
            sterm=record.recorder()
            wb.open("https://www.youtube.com/results?search_query=" + sterm)
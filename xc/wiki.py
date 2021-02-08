import wikipedia
import pyttsx3
import record
eng = pyttsx3.init()
voice_in=record.recorder()
def wikipedia_():
    eng.say("What do you want to search about?")
    eng.runAndWait()
    aud = voice_in()
    eng.say("Searching.....")
    eng.runAndWait()
    result = wikipedia.summary(aud,sentences = 2)
    eng.say('According to Wikipedia')
    eng.runAndWait()
    print(result)
    eng.say(result)
    eng.runAndWait()
wikipedia_()
import time
import pyttsx3
import record

eng=pyttsx3.init()

def enter():
    eng.say("What shall I remind you about?")
    eng.runAndWait()
    voice_in = record.recorder()
    print("Please type, in how many minutes should I remind you?")
    eng.say("Please type, in how many minutes should I remind you?")
    eng.runAndWait()
    ilocal_time = float(input())
    local_time = ilocal_time * 60
    eng.say("I will remind you in:"+str(ilocal_time)+" minutes.")
    eng.runAndWait()
    time.sleep(local_time)
    print("Gentle Reminder: "+voice_in)
    eng.say("Gentle Reminder! "+voice_in)
    eng.runAndWait()
    check=1
    return check
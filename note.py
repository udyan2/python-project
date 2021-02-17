import subprocess
import pyttsx3
import record
import os
eng = pyttsx3.init()
def enter():
    while True:
        eng.say("What should I note?")
        eng.runAndWait()
        voice_in = record.recorder()
        file_name = "C:/Users/"+os.getlogin()+"/Documents/xnote.txt"
        with open(file_name,"a") as f:
            f.write(voice_in)
        subprocess.Popen(["notepad.exe", file_name])
        subprocess.Popen.terminate()
        eng.say("Would you like me to add something to this note?")
        eng.runAndWait()
        voice_in=record.recorder()
        if voice_in.lower()=='yes':
            pass
        else:
            check=1
            return check
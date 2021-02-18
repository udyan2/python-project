import os
import pyttsx3
eng = pyttsx3.init()
def enter():
    eng.say("Opening Word....")
    eng.runAndWait()
    msworld = r"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
    os.startfile(msworld)
    check=1
    return check
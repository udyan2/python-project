import os
import pyttsx3
eng = pyttsx3.init()
def enter():
    eng.say("Xceleron: Opening Excel.")
    eng.runAndWait()
    msexcel = r"C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"
    os.startfile(msexcel)
    check=1
    return check
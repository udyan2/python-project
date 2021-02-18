import os
import pyttsx3
eng = pyttsx3.init()
def enter():
    eng.say("Opening VSCode.")
    eng.runAndWait()
    Vscode = r"C:/Users/LENOVO/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    os.startfile(Vscode)
    check=1
    return check

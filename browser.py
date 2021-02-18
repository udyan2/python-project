import webbrowser
import pyttsx3
eng=pyttsx3.init()

def enter():
    print("Xceleron: Opening the Web Browser.")
    eng.say("Opening the Web Browser.")
    eng.runAndWait()
    webbrowser.open("google.com")
    check=1
    return check
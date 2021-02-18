from subprocess import call
import pyttsx3
eng=pyttsx3.init()
def enter():
    print("Xceleron: Opening the calculator.")
    eng.say("Opening the calculator.")
    eng.runAndWait()
    call(["calc.exe"])
    check=1
    return check
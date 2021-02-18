import pyautogui
import pyttsx3
import os
eng = pyttsx3.init()
def enter():
    img = pyautogui.screenshot()
    img.save("C:/Users/"+os.getlogin()+"/Documents/screenshot.png")
    print("Xceleron: Screenshot taken and saved in documents folder.")
    eng.say("Screenshot taken and saved in documents folder.")
    eng.runAndWait()
    check=1
    return check
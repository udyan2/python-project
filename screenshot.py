import pyautogui
import pyttsx3
eng = pyttsx3.init()
def screenshot():
    img = pyautogui.screenshot()
    img.save('F:/screenshot.png')
    eng.say("Xceleron: Done!")
    eng.runAndWait()
    check=1
    return check
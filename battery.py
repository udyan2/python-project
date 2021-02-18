import psutil #pip
import pyttsx3

eng = pyttsx3.init()
def battery_():
    battery = psutil.sensors_battery()
    bt='The battery is at'+str(battery.percent)+'percent'
    print("Xceleron: "+bt)
    eng.say(bt)
    eng.runAndWait()
    check=1
    return check
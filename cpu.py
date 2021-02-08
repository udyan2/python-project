import psutil #pip
import pyttsx3

eng = pyttsx3.init()
def cpuusage():
    usage = str(psutil.cpu_percent())
    eng.say('CPU utilization is at'+usage+'percent')
    eng.runAndWait()
    check=1
    return check
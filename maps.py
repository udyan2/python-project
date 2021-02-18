import webbrowser as wb
import pyttsx3
import record

eng = pyttsx3.init()


def enter():
    c=0
    while True:
        print("Xceleron: Please tell me the name of the location to search.")
        eng.say("Please tell me the name of the location to search.")
        eng.runAndWait()
        voice_in=(record.recorder()).lower()
        if voice_in=='exit':
            break
        elif len(voice_in)>0:
            print("Xceleron: Searching for "+voice_in+" on Google Maps")
            eng.say('Searching for '+voice_in+' on Google Maps') 
            eng.runAndWait()
            wb.open('https://www.google.com/maps/place/' + voice_in)
            break
        else:
            if c<4:
                print("Xceleron: Could you please repeat the name of the location again?")
                eng.say('Could you please repeat the name of the location again?') 
                eng.runAndWait()
                c+=1
            else:
                break
    check=1
    return check
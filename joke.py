import pyjokes
import pyttsx3
import random
eng = pyttsx3.init()
def jokes():
    lst=['Listen to this hilarious joke','listen to this amazing joke','listen to this funny joke']
    eng.say(random.choice(lst))
    joke = pyjokes.get_joke()
    eng.say(joke)
    eng.runAndWait()
    check=1
    return check
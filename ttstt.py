import speech_recognition as sr
from gtts import gTTS 
import os
import playsound

#from win32com.client import Dispatch

#speak = Dispatch("SAPI.SpVoice")

#speak.Speak("I'm sorry I did not recognize what you said.")
#speak.Speak("How may I help you!")

r=sr.Recognizer()
with sr.Microphone() as source:
    print('say something')
    audio = r.listen(source)
    voice_in=r.recognize_google(audio)
    print(voice_in)
    
  
# Language in which you want to convert 
language = 'en-uk'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=voice_in, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("files123.mp3") 
playsound.playsound("files123.mp3")
os.remove("files123.mp3")
# Playing the converted file 
#   os.system("ttsf.mp3") 
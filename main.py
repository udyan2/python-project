import pyttsx3
import record
import moduleswitcher as ms
import greetings
eng = pyttsx3.init()

eng.say(greetings.greet()+" Hellllo my name is X celeron! How may I help you?")
eng.runAndWait()
voice_in=record.recorder()
ms.shifter(voice_in)

#Change voice between male and female
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#for voice in voices:
#   print(voice)
#   engine.setProperty('voice', voice.id)
#Change voice end
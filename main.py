import pyttsx3
import record
import moduleswitcher as ms
import greetings
eng = pyttsx3.init()

print("Xceleron:",greetings.greet()+" My name is Xceleron!")
eng.say(greetings.greet()+" My name is X celeron!")
eng.runAndWait()

flag=1
while flag==1:
    print("Xceleron: How may I help you?")
    eng.say("How may I help you?")
    eng.runAndWait()
    voice_in=record.recorder()
    flag=ms.shifter(voice_in)


# while(check==1):
#     eng.say("How may I help you?")
#     eng.runAndWait()
#     voice_in=record.recorder
#     ms.shifter(voice_in)

#Change voice between male and female
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#for voice in voices:
#   print(voice)
#   engine.setProperty('voice', voice.id)
#Change voice end1
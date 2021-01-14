import pyttsx3
import searchengine
import record

eng = pyttsx3.init()

def shifter(voice_in):
    emotion_list=["tolk","talk to me","let's talk","let us talk","talk with me","we should talk"]
    search_list=['search something for me','search something',"let's do a search",'perform a search','search for me','do a search','search','i want to perform a search']
    webbrowser_list=['open a website', 'open google chrome for me', 'open chrome','open the browser', 'Visit a website', 'go to a website for me']
    generalq_list=['what is your name','how much do you earn','what is your favourite hobby', 'do you like listening to music','what is your favorite song']
    music_list=['play music','music','i want to listen to music','play some music','music time','play songs','songs time','song time','i want to listen to songs', 'i want some music in life', 'play me something','play music']
    if voice_in.lower() in emotion_list:
        eng.say("Switching to Emotions Module")
        eng.runAndWait()
        #emotions.enter()
    elif voice_in.lower() in search_list:
        eng.say("Switching to Search Module")
        eng.runAndWait()
        searchengine.searchm()
    elif voice_in.lower() in webbrowser_list:
        eng.say("Switching to webbrowser Module")
        eng.runAndWait()
        #browser.enter()
    elif voice_in.lower() in generalq_list:
        eng.say("Switching to General Questions Module")
        eng.runAndWait()
        #generalq.enter
    elif voice_in.lower() in music_list:
        eng.say("Switching to Music Module")
        eng.runAndWait()
        #generalq.enter
    else:
        eng.say("Module not found")
        eng.runAndWait()
eng.say("Hellllo my name is X celeron! How may I help you?")
eng.runAndWait()
voice_in=record.recorder()
shifter(voice_in)



#Change voice between male and female
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#for voice in voices:
#   print(voice)
#   engine.setProperty('voice', voice.id)
#Change voice end
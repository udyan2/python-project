# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:08:48 2021

@author: Udyan Sharma
"""
#For switching to different modules
import pyttsx3
import cpu
import searchengine
import emotions
import battery
import joke
import maps
eng = pyttsx3.init()


def shifter(voice_in):
    emotion_list=["talk","talk to me","let's talk","let us talk","talk with me","we should talk"]
    search_list=['search something for me','search something',"let's do a search",'perform a search','search for me','do a search','search','i want to perform a search']
    webbrowser_list=['open a website', 'open google chrome for me', 'open chrome','open the browser', 'Visit a website', 'go to a website for me']
    generalq_list=['what is your name','how much do you earn','what is your favourite hobby', 'do you like listening to music','what is your favorite song']
    music_list=['play music','music','i want to listen to music','play some music','music time','play songs','songs time','song time','i want to listen to songs', 'i want some music in life', 'play me something','play music']
    wikipedia_list=['search in Wikipedia', 'search something on wikipedia','wikipedia',"find information for me on wikipedia", "wikipedia search","perform a wikipedia search"]
    battery_list=['Show the cpu battery','show system battery', 'show battery','tell system battery','tell cpu battery','show cpu battery']
    cpu_list=['show cpu usage','cpu usage','cpu percent','show cpu percent','tell cpu utilization','tell cpu usage']
    jokes_list=["tell me a joke", "give me a joke","tell a joke","jokes","good joke"]
    exit_list=["exit","quit","bye","shutdown","go to sleep"]
    maps_list=["find this loction for me","where is this place","give me direction to the place","where is this place","find this place for me","does this place exist","check a location for me","open maps for me","open maps","show me a location"]
    note_list=["can you make notes of these","write some notes for me","make some notes","can you sum it up","can you make summary of this","summarise these points","summarise it"]
    reminder_list=["can you remind me of something","remind me","put up a reminder","reminder","remind me this","keep a reminder"]
    notepad_list=["write a note for me","note this down","keep this noted","please note this down","can you note this down","note this down","note"]
    calender_list=["what is todays date"]
    sudoku_list=["let us play something","can we play sudoku","I am bored can we play something","let us do something fun"]
    msword_list=["open a word file","create a new word file","new word document","open word"]
    msexcel_list=["open a excel file","create a new excel file","new excel document","open excel"]
    vscode_vscode=["open a vscode file","create a new vscode file","open vscode","open a vs code file","create a new vs code file","open vs code"]
    news_list=["what are the top news","catch me up with the news","news updates","news updates please","news","tell me about the news","what are the head lines today","whats happening today in the world"]
    system_list=["shutdown the system","shutdown","close my system","we can wrap it up for the day","restart the system","restart","restart my system","logout of the system","logout","logout my system"]
    screenshot_list=["take a screenshot for me","screenshot this","take screenshot","screenshot","let us screenshot that"]
    timer_list=["open timer","open up the timer","open the timer"]
    if voice_in.lower() in emotion_list:
        # eng.say("Switching to Emotions Module")
        # eng.runAndWait()
        check=emotions.enter()
        return check
    elif voice_in.lower() in search_list:
        # eng.say("Switching to Search Module")
        # eng.runAndWait()
        check=searchengine.searchm()
        return check
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
    elif voice_in.lower() in wikipedia_list:
        eng.say("Switching to Wikipedia module")
        eng.runAndWait()
    elif voice_in.lower() in cpu_list:
        # eng.say("Switching to cpu module")
        # eng.runAndWait()
        check=cpu.cpuusage()
        return check
    elif voice_in.lower() in battery_list:
        # eng.say("Switching to battery module")
        # eng.runAndWait()
        check=battery.battery_()
        return check
    elif voice_in.lower() in jokes_list:
        # eng.say("Switching to Jokes Module")
        # eng.runAndWait()
        check=joke.jokes()
        return check
    elif voice_in.lower() in maps_list:
        # eng.say("Switching to Jokes Module")
        # eng.runAndWait()
        check=maps.enter()
        return check
    # elif voice_in.lower() in jokes_list:
    #     # eng.say("Switching to Jokes Module")
    #     # eng.runAndWait()
    #     check=joke.jokes()
    #     return check
    elif voice_in.lower() in exit_list:
        eng.say("Bye, have a great day!")
        eng.runAndWait()
    else:
        eng.say("This functionality will be available soon!")
        eng.runAndWait()
        return 1

from urllib.request import urlopen
import json
import pyttsx3

eng=pyttsx3.init()

def readnews():
    try:
        jsonObj = urlopen('''http://newsapi.org/v2/top-headlines?country=in&apiKey=482e97f9a721485bbc540c3cd38510e3''')
        data = json.load(jsonObj)
        i = 0
        
        print('Xceleron: Here are the top 5 headlines for today:')
        eng.say('Here are the top 5 headlines for today.')
        eng.runAndWait()
        print('''=============== TOP HEADLINES ============'''+ '\n')
        while i<5:
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                eng.say(str(i) + '. ' + item['title'] + '\n')
                eng.runAndWait()
                i += 1
                         
    except Exception as e:
        print("Xceleron: "+str(e))

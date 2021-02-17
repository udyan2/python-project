from datetime import date
import pyttsx3

eng=pyttsx3.init()

def enter():       
    today = date.today()
# dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print(d1)
    eng.say("The date[ today is, "+d1)
    eng.runAndWait()

    if d1 == "01/01/2021":            
        print("Happy New Year")
        eng.say("Happy New Year")
        eng.runAndWait()

    elif d1 == "13/01/2021":
        print("Happy Lohri")
        eng.say("Happy Lohri")
        eng.runAndWait()
    
    elif d1 == "14/01/2021":
        
        print("Happy Makar Sakranti")
        eng.say("Happy Makar Sakranti")
        eng.runAndWait()
    
    elif d1 == "20/01/2021":
        print("Guru Gobind Singh Jayanti")
        eng.say("Guru Gobind Singh Jayanti")
        eng.runAndWait()
    
    elif d1 == "26/01/2021":
        print("Happy Republic Day")
        eng.say("Happy Republic Day")
        eng.runAndWait()
        
    elif d1 == "16/02/2021":
        print("Vasant Panchami")
        eng.say("Vasant Panchami")
        eng.runAndWait()
        
    elif d1 == "11/03/2021":
        print("Maha-Shivratari")
        eng.say("Maha-Shivratari")
        eng.runAndWait()
    
    elif d1 == "29/03/2021":
        print("Happy Holi")
        eng.say("Happy Holi")
        eng.runAndWait()
    
    elif d1 == "02/04/2021":
        print("A very happy Good Friay to You")
        eng.say("A very happy Good Friay to You")
        eng.runAndWait()
    
    elif d1 == "04/04/2021":
        print("Wishing YOu a Very Happy Easter Day")
        eng.say("Wishing YOu a Very Happy Easter Day")
        eng.runAndWait()
        
    elif d1 == "21/04/2021":
        print("Happy Ram-Navmi")
        eng.say("Happy Ram-Navmi")
        eng.runAndWait()
        
    elif d1 == "25/04/2021":
        print("Happy Mahavir Jayanti")
        eng.say("Happy Mahavir Jayanti")
        eng.runAndWait()
        
    elif d1 == "13/05/2021":
        print("May Allah Shower his mercy on this Ramdan upon you and your family")
        eng.say("May Allah Shower his mercy on this Ramdan upon you and your family")
        eng.runAndWait()
        
    elif d1 == "20/07/2021":
        print("Wishing You a blessed Bakar-id")
        eng.say("Wishing You a blessed Bakar-id")
        eng.runAndWait()
        
    elif d1 == "15/08/2021":
        print("Happy  Independence Day")
        eng.say("Happy  Independence Day")
        eng.runAndWait()

    elif d1 == "19/08/2021":
        print("Happy Muharram")
        eng.say("Happy Muharram")
        eng.runAndWait()
        
    elif d1 == "21/08/2021":
        print("Happy Onam")
        eng.say("Happy Onam")
        eng.runAndWait()
        
    elif d1 == "22/08/2021":
        print("Sending you loads of Love and Greetings, Happy Raksha Bandhan")
        eng.say("Sending you loads of Love and Greetings, Happy Raksha Bandhan")
        eng.runAndWait()
        
    elif d1 == "30/08/2021":
        print("May all Your Prayers be answered, Happy Janamashtami")
        eng.say("May all Your Prayers be answered, Happy Janamashtami")
        eng.runAndWait()
        
    elif d1 == "10/09/2021":
        print("May god Ganesha bless you and your family with Lots of wisdom and fortune, Happy Ganesh Chaturthi")
        eng.say("May god Ganesha bless you and your family with Lots of wisdom and fortune, Happy Ganesh Chaturthi")
        eng.runAndWait()
        
    elif d1 == "02/10/2021":
        print("Happy Mahatama Gandhi Jayanti")
        eng.say("Happy Mahatama Gandhi Jayanti")
        eng.runAndWait()

    elif d1 == "15/10/2021":
        print("May This Dussehra bring lots of light and Happiness in your life")
        eng.say("May This Dussehra bring lots of light and Happiness in your life")
        eng.runAndWait()
        
    elif d1 == "04/11/2021":
        print("May God Light up your future, Happy Diwali")
        eng.say("May God Light up your future, Happy Diwali")
        eng.runAndWait()
        
    elif d1 == "25/12/2021":
        print("Merry Christmas")
        eng.say("Merry Christmas")
        eng.runAndWait()
    
    elif d1 == "31/12/2021":
        print("I hope you Party Hard and Enjoy yourself today, Gear up for the new Year's Eve")
        eng.say("I hope you Party Hard and Enjoy yourself today, Gear up for the new Year's Eve")
        eng.runAndWait()
    check=1
    return check
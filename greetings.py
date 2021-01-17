import datetime as dt

def greet(): 
    if dt.datetime.today().hour>=0 and dt.datetime.today().hour<6:
        return "It is late at night."
    if dt.datetime.today().hour>=6 and dt.datetime.today().hour<12:
        return "Good morning!"
    elif dt.datetime.today().hour>=12 and dt.datetime.today().hour<18:
        return "Good afternoon!"
    elif dt.datetime.today().hour>=18 and dt.datetime.today().hour<22:
        return "Good evening!"
    elif (dt.datetime.today().hour>=22 and dt.datetime.today().hour<=24) or dt.datetime.today().hour==0:
        return "It's night"
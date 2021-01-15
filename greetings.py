import datetime as dt

if dt.datetime.today().hour>=6 and dt.datetime.today().hour<12:
    print("Good Morning")
if dt.datetime.today().hour>=12 and dt.datetime.today().hour<18:
    print("Good Afternoon")
if dt.datetime.today().hour>=18 and dt.datetime.today().hour<22:
    print("Good Evening")
if (dt.datetime.today().hour>=22 and dt.datetime.today().hour<=24) or dt.datetime.today().hour==0:
    print("It's midnight")
if(dt.datetime.today())==today.time()
import record
import pyttsx3
import tkinter as tk
from tkinter import filedialog
import pandas as pd

eng=pyttsx3.init()

def enter():
    def trainmodel():
        root= tk.Tk()
        traincanvas = tk.Canvas(root, width = 300, height = 300, bg = 'white')
        traincanvas.pack()
    
        def getExcel ():
            global rf, angry, sad, love, surprise, joy, fear
            
            import_file_path = filedialog.askopenfilename()
            rf = pd.read_excel (import_file_path)
            
            angry = rf['Angry'].tolist()
            sad = rf['Sad'].tolist()
            love = rf['Love'].tolist()
            surprise = rf['Fear'].tolist()
            joy = rf['Joy'].tolist()
            fear = rf['Fear'].tolist()
           
        browseb_Excel = tk.Button(text='Train Model', command=getExcel, bg='green', fg='white', font=('arial', 12, 'bold'))
        traincanvas.create_window(150, 150, window=browseb_Excel)
        root.mainloop()
        return
    
    score=[0,0,0,0,0]
    vw_list=["i","am","is","was","in","up","and","a","he","she","we","see","something","more","than","the","my","by","all","of","you","feeling","such","day","today","it" ,"sent"]
    flag=1
    while(flag==1):
        print("Xceleron: I am here to talk to you! So, how are you feeling?")
        eng.say("i am here to talk to you! So, how are you feeling")
        eng.runAndWait()
        
        file_path='emotions.xlsx'
        rf = pd.read_excel (file_path)
    
        angry = rf['Angry'].str.lower().tolist()
        sad = rf['Sad'].str.lower().tolist()
        love = rf['Love'].str.lower().tolist()
        joy = rf['Joy'].str.lower().tolist()
        fear = rf['Fear'].str.lower().tolist()
        # res_angry = rf['Response_Anger'].str.lower().tolist()
        # res_sad = rf['Response_Sad'].str.lower().tolist()
        # res_love = rf['Response_Love'].str.lower().tolist()
        # res_joy = rf['Response_Joy'].str.lower().tolist()
        # res_fear = rf['Response_Fear'].str.lower().tolist()
            
            
        voice_in = record.recorder()
        words_in = voice_in.lower().split()
        print("Xceleron: ",words_in)
        
        for el in words_in:
            if el not in vw_list:
                check_angry = rf['Angry'].str.contains(el).any()
                check_sad = rf['Sad'].str.contains(el).any()
                check_love = rf['Love'].str.contains(el).any()
                # check_surprise = rf['Surprise'].str.contains(voice_in.lower()).any()
                check_joy = rf['Joy'].str.contains(el).any()
                check_fear = rf['Fear'].str.contains(el).any()
            
                if voice_in == 'train model':
                    print("Xceleron: I love training. Please provide me with the excel file.")
                    eng.say("I love training. Please provide me with the excel file.")
                    eng.runAndWait()
                    trainmodel()
                    break
                elif check_angry:
                    score[0]+=1
                    print("Xceleron: (",el,") I sense anger. Calm down.")
                    eng.say("I sense anger. Calm down.")
                    eng.runAndWait()
                elif check_sad:
                    score[1]+=1
                    print("Xceleron: (",el,") I sense sadness. I am so sorry.")
                    eng.say("I sense sadness. I am so sorry.")
                    eng.runAndWait()
                elif check_love:
                    score[2]+=1
                    print("Xceleron: (",el,") I sense love. It's great.")
                    eng.say("I sense love. It's great.")
                    eng.runAndWait()
                #elif check_surprise:
                #    eng.say("you look do surprised.")
                #    eng.runAndWait()
                elif check_joy:
                    score[3]+=1
                    print("Xceleron: (",el,") I sense joy. I am so happy for you.")
                    eng.say("I sense joy. I am so happy for you.")
                    eng.runAndWait()
                elif check_fear:
                    score[4]+=1
                    print("Xceleron: (",el,") I sense fear. Don't worry, I am here.")
                    eng.say("I sense fear. Don't worry, I am here.")
                    eng.runAndWait()
                elif voice_in.lower()=='exit':
                    print("Xceleron: Exiting Emotions Module")
                    eng.say("Exiting Emotions Module")
                    eng.runAndWait()
                    check=1
                    return check                
                else:
                    print("not found")
        print("Xceleron: Would you like me to show your emotions score?")
        eng.say("Would you like me to show your emotions score?")
        eng.runAndWait()
        voice_in=record.recorder()
        if voice_in.lower()=='yes':
            print("Angry:", score[0],
                  "\nSad:", score[1],
                  "\nLove:", score[2],
                  "\nJoy:", score[3],
                  "\nFear:", score[4])
            check=1
            return check
        else:
            pass
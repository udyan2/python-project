import tkinter as tk
from tkinter import filedialog
import pandas as pd


def getExcel ():
    global rf
    import_file_path = filedialog.askopenfilename()
    rf = pd.read_excel (import_file_path)
    angry = rf['Angry'].tolist()
    sad = rf['Sad'].tolist()
    love = rf['Love'].tolist()
    surprise = rf['Fear'].tolist()
    joy = rf['Joy'].tolist()n
    fear = rf['Fear'].tolist()
    print("Angry:",angry)
    print("Sad:",sad)
    print("Love:",love)
    print("Surprise:",surprise)
    print("Joy:",joy)
    print("Fear:",fear)
    
    
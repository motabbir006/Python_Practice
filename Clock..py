from tkinter import*
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Digital Clock")
def time():
    from datetime import datetime
    n = datetime.now()

    string = n.strftime(" %D:%H:%M:%S")
    print(string)


    label.config(text=string)
    label.after(1000,time)

label= Label(root,font=("ds-digital", 180), background="Green", foreground= "Red")
label.pack(anchor='center')
time()
mainloop()
import tkinter
from math import *

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x480+100+100")
window.resizable(False, False)

def calc(event):
    label.config(text="결과="+str(eval(entry.get())))
    

entry=tkinter.Entry(window , text ="123")
entry.bind("<Return>", calc)
entry.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()
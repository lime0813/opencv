import tkinter
import tkinter.font as tk_font

window = tkinter.Tk()
window.title("test")
window.geometry("640x480+100+100")

font = tkinter.font.Font(family = "맑은 고딕" , size = 20)
def change(entry,label):
    s = entry.get()
    label.config(text = s)
class 만들기():
    def __init__(self,name):
        self.name = name

    def 라벨만들기(self):
        print(self.name)

for i in range(2):
    entry = tkinter.Entry(window , font = font)
    entry.pack()

    button = tkinter.Button(window,text = "실행",font = font, command = lambda: change(entry,label))
    button.pack()

    label = tkinter.Label(window , text = "결과1", font = font)
    label.pack()

window.mainloop()

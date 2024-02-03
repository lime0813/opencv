import tkinter
import tkinter.font as tk_font
import face
import cat
import pose

window = tkinter.Tk()
window.title("인식하기 기능 버튼 만들기")
window.geometry("640x400+100+100")
window.resizable(False,False)
font = tk_font.Font(family="맑은 고딕",size = 20)

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)

window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)

face_button = tkinter.Button(window , text = "얼굴인식" , font = font , command= face.face_func)
face_button.grid(column = 0,row = 0,sticky="nsew")

pose_button = tkinter.Button(window , text = "포즈인식" , font = font , command= pose.pose_func)
pose_button.grid(column = 0,row = 1,sticky="nsew")

catface_button = tkinter.Button(window , text = "고영희" , font = font , command= cat.cat_func)
catface_button.grid(column = 1,row = 0,sticky="nsew")

hand_button = tkinter.Button(window , text = "손인식" , font = font)
hand_button.grid(column = 1,row = 1,sticky="nsew")

window.mainloop()
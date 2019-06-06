import tkinter.font
from tkinter import *

def quit():
    button1.config(state='normal')

    newwin.destroy()

def disable_event():
    pass

def new_winF(): # new window definition

    global button1
    button1.config(state='disabled')

    global newwin
    newwin = Toplevel(window)
    newwin.geometry("300x300")
    newwin.resizable(False, False)

    font = tkinter.font.Font(family="맑은 고딕", size=20)
    label = tkinter.Label(newwin, text="문제를 풀어보세요!!", width=30, height=2, fg="red", font=font)
    label.pack()
    btn1 = tkinter.Button(newwin, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100, text = "종료", command=quit)
    btn1.place(x=40, y=250)
    newwin.protocol("WM_DELETE_WINDOW", disable_event)




window = tkinter.Tk()
window.title("warming-up")
window.geometry("500x300")
window.resizable(False, False)

font = tkinter.font.Font(family="맑은 고딕", size=20)
label = tkinter.Label(window, text="문제를 풀어보세요!!", width=30, height=2, fg="red", font=font)
label.pack()

button1 = tkinter.Button(window, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100, text="시작"
                         , command=new_winF)
button1.config(state='normal')

button1.pack()
window.mainloop()

import random
import tkinter.font
from tkinter import *


def quit():
    button1.config(state='normal')
    newwin.destroy()


def clear():
    textbox.delete(0, END)


def new_winF():
    button1.config(state='disabled')

    global newwin
    newwin = Toplevel(window)
    newwin.geometry("300x250")
    newwin.resizable(False, False)

    font = tkinter.font.Font(family="맑은 고딕", size=20)
    global label
    label = Label(newwin, text="문제", width=30, height=2, fg="black", font=font)
    label.pack()
    newwin.protocol("WM_DELETE_WINDOW", quit)
    mkproblem()

    global textbox
    textbox = Entry(newwin, width=20, textvariable=str)
    textbox.pack()

    btn2 = tkinter.Button(newwin, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100,
                          text="제출", command=check)

    btn2.pack(padx=10, pady=10)
    btn1 = tkinter.Button(newwin, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100,
                          text="종료", command=quit)
    btn1.pack(padx=10, pady=10)


def mkproblem():
    global x
    global y
    global op_int
    global answer
    x = random.randrange(2, 1001)
    y = random.randrange(2, 1001)
    op_int = random.randrange(1, 5)
    if (op_int == 1):
        op_str = "+"
        question = str(x) + " " + op_str + " " + str(y) + " = ??"
        answer = x+y
    elif (op_int == 2):
        op_str = "-"
        if (y > x):
            x, y = exchange(x, y)
        question = str(x) + " " + op_str + " " + str(y) + " = ??"
        answer = x - y
    elif (op_int == 3):
        x = random.randrange(2, 11)
        y = random.randrange(2, 11)
        op_str = "*"
        question = str(x) + " " + op_str + " " + str(y) + " = ??"
        answer = x * y
    elif (op_int == 4):
        x = random.randrange(2, 11)
        y = random.randrange(2, 11)
        if (y > x):
            x, y = exchange(x, y)
        op_str = "÷"
        question = str(x) + " " + op_str + " " + str(y) + " = " + str((int)(x / y)) + "...??"
        answer = x % y

    elif (op_int == 5):
        x = random.randrange(2, 11)
        y = random.randrange(2, 11)
        if (y > x):
            x, y = exchange(x, y)
        op_str = "÷"
        question = str(x) + " " + op_str + " " + str(y) + " = ??..." + str((int)(x % y))
        answer = x / y

    print("X ",x,"y",y,"answer",answer)
    label.configure(text=question)


def exchange(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def check():
    global answer
    print(textbox.get())
    print(answer)
    print(type(answer))
    print(type(textbox.get()))
    if(textbox.get() !=""):
        if(answer == (int)(textbox.get())):
            print("!!")
            mkproblem()
            clear()


window = tkinter.Tk()
window.title("warming-up")
window.geometry("400x250")
window.resizable(False, False)

textbox = tkinter.Entry

font = tkinter.font.Font(family="맑은 고딕", size=20)
label = tkinter.Label(window, text="머리를 풀어보세요!!", width=30, height=2, fg="red", font=font)
label.pack()

button1 = tkinter.Button(window, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100, text="시작"
                         , command=new_winF)
button1.config(state='normal')
button1.pack()

window.mainloop()
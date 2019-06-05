import tkinter.font
import tkinter

def disabled():
    button1.config(state='disabled')
    button2.config(state='disabled')
    button3.config(state='disabled')

def normal():
    button1.config(state='normal')
    button2.config(state='normal')
    button3.config(state='normal')

def beginner():
    problem = tkinter.Tk()
    window.protocol("WM_DELETE_WINDOW", normal)
    disabled()

def Intermediate():
    problem = tkinter.Tk()
    window.protocol("WM_DELETE_WINDOW", normal)
    disabled()

def Advanced():
    problem = tkinter.Tk()
    window.protocol("WM_DELETE_WINDOW", normal)
##########
    #disabled()


window = tkinter.Tk()
window.title("warming-up")
window.geometry("500x300")
window.resizable(False, False)

font = tkinter.font.Font(family="맑은 고딕", size=20)
label = tkinter.Label(window, text="문제를 풀어보세요!!", width=30, height=2, fg="red", font=font)
label.pack()

button1 = tkinter.Button(window, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100, text="초급"
                         , command=beginner)
button1.pack(pady = 10)

button2 = tkinter.Button(window, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100, text="중급"
                         , command=Intermediate)
button2.pack(pady = 10)

button3 = tkinter.Button(window, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100, text="고급"
                         , command=Advanced)
button3.pack(pady = 10)


window.mainloop()

if(window.destroy()):
    normal()
import tkinter.font
from tkinter import *
from numpy import *
import pygame
import random


# 음악 재생 필수요소
def note2array(freq, len, amp=1., rate=44100):
    t = arange(len*rate)/float(rate)
    data = sin(2*pi*freq*t)*amp
    return data.astype(int16)

# 음악 재생
def sound_play(data, rate=44100):
    pygame.mixer.pre_init(rate, -16, 1, 4096)
    pygame.mixer.init()
    sound = pygame.sndarray.make_sound(data)
    length = sound.get_length()
    sound.play()
    pygame.time.wait(int(length * 1000))
    pygame.mixer.quit()

# 음악 음계 모음
def sound(check):
    fs = 8000
    dur = 0.5

    freq_of_tones = array([]).astype(int16)

    # 도0 레2 미4 피5 솔7 라9 시11 도12 높은레 14 높은미 16 높은 파 17 높은 솔19
    # 높은 라21 높은 시23 더 높은 도 24
    if check:
        for n in [0, 4, 7, 12]:
            f = int(440 * pow(2., n / 12.) + 0.5)
            freq_of_tones = append(freq_of_tones, note2array(freq=f, len=dur, amp=32767 - 10000., rate=fs))
        sound_play(freq_of_tones, rate=fs)
        # print("맞")

    else:
        for n in [12]:
            f = int(440 * pow(2., n / 12.) + 0.5)
            freq_of_tones = append(freq_of_tones, note2array(freq=f, len=dur, amp=32767 - 10000., rate=fs))
        sound_play(freq_of_tones, rate=fs)
        # print("틀")

# 버튼으로 종료 함수
def end():
    button1.config(state='normal')
    newwin.destroy()


# 문제 창 생성
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
    newwin.protocol("WM_DELETE_WINDOW", end)
    mkproblem()

    global textbox
    textbox = Entry(newwin, width=20, textvariable=str)
    textbox.pack()

    btn2 = tkinter.Button(newwin, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100,
                          text="제출", command=check)

    btn2.pack(padx=10, pady=10)
    btn1 = tkinter.Button(newwin, overrelief="solid", width=30, height=2, repeatdelay=1000, repeatinterval=100,
                          text="종료", command=end)
    btn1.pack(padx=10, pady=10)

# 문제 생성 및 정답 저장
def mkproblem():
    x = random.randrange(2, 1001)
    y = random.randrange(2, 1001)
    op_int = random.randrange(1, 5)

    global answer

    if op_int == 1:
        op_str = "+"
        question = str(x) + " " + op_str + " " + str(y) + " = ??"
        answer = x + y

    elif op_int == 2:
        op_str = "-"
        if y > x:
            x, y = y, x
        question = str(x) + " " + op_str + " " + str(y) + " = ??"
        answer = x - y

    elif op_int == 3:
        x = random.randrange(2, 11)
        y = random.randrange(2, 11)
        op_str = "*"
        question = str(x) + " " + op_str + " " + str(y) + " = ??"
        answer = x * y

    elif op_int == 4:
        x = random.randrange(2, 11)
        y = random.randrange(2, 11)
        if y > x:
            x, y = y, x
        op_str = "÷"
        question = str(x) + " " + op_str + " " + str(y) + " = " + str(int(x / y)) + "...??"
        answer = x % y

    elif op_int == 5:
        x = random.randrange(2, 11)
        y = random.randrange(2, 11)
        if y > x:
            x, y = y, x
        op_str = "÷"
        question = str(x) + " " + op_str + " " + str(y) + " = ??..." + str(int(x % y))
        answer = x / y

    print("X ",x,"y",y,"answer",answer)
    label.configure(text=question)

# 정답 체크
def check():
    # print(answer)
    if textbox.get() != "":
        if answer == int(textbox.get()):
            print("!!")
            mkproblem()
            textbox.delete(0, END)
            sound(True)
        else:
            sound(False)


# 시작 윈도우 생성
def create_window():
    global window
    window = tkinter.Tk()
    window.title("warming-up")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_x = (screen_width / 2) - (400 / 2)
    window_y = (screen_height / 2) - (250 / 2)
    window.geometry('%dx%d+%d+%d' % (400, 240, window_x, window_y))
    window.resizable(False, False)


# 시작 윈도우 셋팅
def window_setting():
    global button1
    textbox = tkinter.Entry
    font = tkinter.font.Font(family="맑은 고딕", size=20)
    label = tkinter.Label(window, text="머리를 풀어보세요!!", width=30, height=2, fg="red", font=font)
    label.pack()

    button1 = tkinter.Button(window, overrelief="solid", width=20, height=3, repeatdelay=1000, repeatinterval=100,
                             text="시작"
                             , command=new_winF, font=font)
    button1.config(state='normal')
    button1.pack()


create_window()
window_setting()
window.mainloop()

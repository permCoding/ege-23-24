from tkinter import *
from random import randint


def step():
    global count, com
    
    try:
        hum = int(ent.get())
        if 99 < hum < 1_000:
            count += 1
            if com == hum: 
                lbl['text'] = f'угадал; шаг - {count}'
            elif com > hum: 
                lbl['text'] = f'больше; шаг - {count}'
            else:
                lbl['text'] = f'меньше; шаг - {count}'
        else:
            lbl['text'] = 'от 100 до 999'
    except:
        lbl['text'] = 'требуется целое число'


def start():
    global com, count
    com = randint(100, 999)
    count = 0
    ent.delete(0, END)
    ent.insert(0, 'тут вводить число')


win = Tk()
win.title("Угадай число")
win.iconbitmap("frog.ico")
win.geometry("500x300+500+200")
win.resizable(False, False)

com, count = 0, 0

lbl = Label(win, font='Consolas 12', width=36, text="- - -")
lbl.pack()

ent = Entry(win, font='Consolas 16 bold', \
    width=20, bg='yellow')
ent.pack()

btnStep = Button(win, font='Consolas 16 bold', \
    width=20, text="Сделать ход", command=step, fg="#009")
btnStep.pack()

btnStart = Button(win, font='Consolas 16 bold', \
    width=20, text="Начать сначала", command=start, bg='#fd6')
btnStart.pack()

start()
win.mainloop()

"""
R G B
R = 0 .. 255 b 00000000
G = 0 .. 255 b
B = 0 .. 255 b
2**8

f - 0000

0 - 0000
1 - 0001
2 - 0010
3
...
A
B
C
D - 
E - 1110
F - 1111

00 - 00
0F - 15
10 - 16
...
FF - 255

#00AA88 == # 0A8 

"""
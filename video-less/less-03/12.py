from tkinter import *
from random import randint


def step():
    global count, com
    
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


def start():
    global com, count
    com = randint(100, 999)
    count = 0


win = Tk()
win.title("Угадай число")
win.iconbitmap("frog.ico")
win.geometry("500x300+500+200")
win.resizable(False, False)

font = 'Consolas 18 bold'
com, count = 0, 0

lbl = Label(win, font=font, width=20, text="- - -")
lbl.pack()

ent = Entry(win, font=font, width=20)
ent.pack()

btn = Button(win, font=font, width=20, text="Сделать ход", command=step)
btn.pack()

btnStart = Button(win, font=font, width=20, text="Начать сначала", command=start)
btnStart.pack()

start()
win.mainloop()

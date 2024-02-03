from tkinter import *
from tkinter import ttk
from random import randint


def step():
    global count, com
    
    if count < 10:
        try:
            hum = int(ent.get())
            if 99 < hum < 1_000:
                count += 1
                pb['value'] = count * 10
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
    else:
        lbl['text'] = 'превышено кол-во ходов'


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

btnStep = Button(win, font='Consolas 16', \
    width=20, text="Сделать ход", command=step, fg="#009")
btnStep.pack()

btnStart = Button(win, font='Consolas 16', \
    width=20, text="Начать сначала", command=start, bg='#fd6')
btnStart.pack()

pb = ttk.Progressbar(win, length=250, orient='horizontal', mode='determinate')
pb.pack()

start()
win.mainloop()

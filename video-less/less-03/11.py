from tkinter import *


def step():
    lbl['text'] = ent.get()

win = Tk()
win.title("Угадай число")
win.iconbitmap("frog.ico")
win.geometry("500x300+500+200")
win.resizable(False, False)

font = 'Consolas 16 bold'

lbl = Label(win, font=font, width=20, text="- - -")
lbl.pack()

ent = Entry(win, font=font, width=20)
ent.pack()

btn = Button(win, font=font, width=20, \
             text="Сделать ход", command=step)
btn.pack()

win.mainloop()

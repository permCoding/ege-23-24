from tkinter import *
from random import randint


def rb_click():
    lbl['text'] = rbs_.get()

def get_rb(num):
    return Radiobutton(win, text=hds[num], value=num, \
        variable=rbs_, command=rb_click)


win = Tk()
win.geometry('600x400')
win.resizable(False, False)
win.iconbitmap('./frog.ico')
win.title('Камень - Ножницы - Бумага')

fonts = ['Consolas 14', 'Consolas 14 bold']
colors = ['black', 'red']
hds = ["Камень", "Ножницы", "Бумага"]

lbl = Label(win, text='- - -', font=fonts[0]); lbl.pack()

rbs_ = IntVar(value=-1)
rbs = [get_rb(i) for i in range(len(hds))]
for rb in rbs: rb.pack()

win.mainloop()
from tkinter import *
from tkinter import ttk


def rb_click():
    lbl['text'] = rbs_.get()

def get_rb(num, frame):
    return Radiobutton(frame, text=hds[num], value=num, \
        variable=rbs_, command=rb_click)


win = Tk()
win.geometry('600x400')
win.resizable(False, False)
win.iconbitmap('./frog.ico')
win.title('Камень - Ножницы - Бумага')

fonts = ['Consolas 14', 'Consolas 14 bold']
colors = ['black', 'red']
hds = ["Камень", "Ножницы", "Бумага"]

for i in 0,1: win.columnconfigure(index=i, weight=1)
for i in 0,1: win.rowconfigure(index=0, weight=1)

frameH = ttk.Frame(relief='flat', padding=[5, 5])
frameH.grid(row=0, column=0)
rbs_ = IntVar(value=-1)
rbs = [get_rb(i, frameH) for i in range(len(hds))]
for rb in rbs: rb.pack(anchor='w')

frameC = ttk.Frame(relief='flat', padding=[5, 5])
frameC.grid(row=0, column=1)
lbl = Label(frameC, text='- - -', font=fonts[0])
lbl.pack()


win.mainloop()
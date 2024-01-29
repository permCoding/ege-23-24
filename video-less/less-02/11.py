from tkinter import *


font = ('Consolas', 16)

win = Tk()
win.geometry('600x400')
win.resizable(False, False)
win.iconbitmap('./frog.ico')
win.title('Камень - Ножницы - Бумага')

btn0 = Button(win, text="Камень", width=20, font=font); btn0.pack()
btn1 = Button(win, text="Ножницы", width=20, font=font); btn1.pack()
btn2 = Button(win, text="Бумага", width=20, font=font); btn2.pack()
lbl1 = Label(win, text=" - - - "); lbl1.pack()

win.mainloop()
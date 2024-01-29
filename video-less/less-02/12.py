from tkinter import *


def get_btn(txt, font):
    return Button(win, text=txt, width=20, font=font)

def get_lbl(txt, font):
    return Label(win, text=txt, font=font)


win = Tk()
win.geometry('600x400')
win.resizable(False, False)
win.iconbitmap('./frog.ico')
win.title('Камень - Ножницы - Бумага')

font = ('Consolas', 14)
hds = ["Камень", "Ножницы", "Бумага"]
btns = [get_btn(elm, font) for elm in hds]
for btn in btns: btn.pack()

lbl1 = get_lbl("Ничья", font); lbl1.pack()
lbl2 = get_lbl("По - 0; Ни - 0; Пр - 0", font); lbl2.pack()

win.mainloop()
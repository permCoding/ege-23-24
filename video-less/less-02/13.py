from tkinter import *


def _print(i):
    print(i)

def get_btn(txt, font, i):
    return Button(win, text=txt, width=20, font=font, \
        command=lambda x=i: _print(x))

def get_lbl(txt, font):
    return Label(win, text=txt, font=font)


win = Tk()
win.geometry('600x400')
win.resizable(False, False)
win.iconbitmap('./frog.ico')
win.title('Камень - Ножницы - Бумага')

font = ('Consolas', 14)
hds = ["Камень", "Ножницы", "Бумага"]
# btns = []
# for i in range(len(hds)):
#     # btns.append(get_btn(hds[i], font, i))
#     btns += [get_btn(hds[i], font, i)]
btns = [get_btn(elm, font, i) for i,elm in enumerate(hds)]
for btn in btns: btn.pack()

lbl1 = get_lbl("Ничья", font); lbl1.pack()
lbl2 = get_lbl("По - 0; Ни - 0; Пр - 0", font); lbl2.pack()

win.mainloop()
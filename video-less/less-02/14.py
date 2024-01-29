from tkinter import *
from random import randint

def get_btn(txt, font, i):
    return Button(win, text=txt, width=20, font=font, \
        command=lambda x=i: step(x))

def get_lbl(txt, font):
    return Label(win, text=txt, font=font)

def get_res():
    return f"По - {res[0]}; Ни - {res[1]}; Пр - {res[2]}"
    
def step(hum):
    com = str(randint(0, 2))
    tmp = str(hum) + com
    if tmp in ['01', '12', '20']:
        res[0] += 1
        msg = "Победа"
    elif tmp in ['10', '21', '02']:
        res[2] += 1
        msg = "Поражение"
    else:
        res[1] += 1
        msg = "Ничья"
    lbl1['text'] = msg
    lbl2['text'] = get_res()


win = Tk()
win.geometry('600x400')
win.resizable(False, False)
win.iconbitmap('./frog.ico')
win.title('Камень - Ножницы - Бумага')

font = ('Consolas', 14)
hds = ["Камень", "Ножницы", "Бумага"]
btns = [get_btn(elm, font, i) for i,elm in enumerate(hds)]
for btn in btns: btn.pack()

res = [0, 0, 0]
lbl1 = get_lbl(" - - - ", font); lbl1.pack()
lbl2 = get_lbl(get_res(), font); lbl2.pack()

win.mainloop()
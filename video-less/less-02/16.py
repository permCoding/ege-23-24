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
    com = randint(0, 2)
    for btn in btns: btn.configure(fg=colors[0])
    btns[com].configure(fg=colors[1])
    tmp = str(hum) + str(com)
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
    
    if res[0] > 4 or res[2] > 4:
        if res[0] > 4:
            lbl1['text'] = "Победил Человек"
        else:
            lbl1['text'] = "Победил Computer"

def start():
    global res
    res = [0, 0, 0]
    lbl1['text'] = " - - - "
    lbl2['text'] = get_res()
    for btn in btns: btn.configure(fg=colors[0])

win = Tk()
win.geometry('600x400')
win.resizable(False, False)
win.iconbitmap('./frog.ico')
win.title('Камень - Ножницы - Бумага')

fonts = ['Consolas 14', 'Consolas 14 bold']
colors = ['black', 'red']
hds = ["Камень", "Ножницы", "Бумага"]
btns = [get_btn(elm, fonts[0], i) for i,elm in enumerate(hds)]
for btn in btns: btn.pack()

lbl1 = get_lbl("", fonts[0]); lbl1.pack()
lbl2 = get_lbl("", fonts[0]); lbl2.pack()
res = [0, 0, 0]
start()

btn_start = Button(win, text="Start", width=20, font=fonts[1], command=start)
btn_start.pack()
btn_close = Button(win, text="Quit", width=20, font=fonts[1], command=win.destroy)
btn_close.pack()

win.mainloop()
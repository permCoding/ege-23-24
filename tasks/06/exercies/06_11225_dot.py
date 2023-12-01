from turtle import *

st = 25
speed(9)
lt(90)

rt(60)

fd(7*st)
rt(120)
fd(7*st)
rt(120)

rt(300)
fd(7*st)

rt(60)
fd(7*st)
rt(60)

rt(60)
fd(7*st)
rt(60)

penup()
for x in range(-150, +200, st):
    for y in range(-200, +150, st):
        setpos(x, y)
        dot(3, 'red')

done()  # 66

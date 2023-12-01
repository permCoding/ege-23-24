from turtle import *

st = 25

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

speed(9)
width(1)
color('red')
x = (10, 140)
y = (100, 240)

x0, y0 = -10*st, -10*st
for x in range(20):
    penup(); goto(x0+x*st, y0)
    pendown(); goto(x0+x*st, y0+20*st)
for y in range(20):
    penup(); goto(x0, y0+y*st)
    pendown(); goto(x0+20*st, y0+y*st)

done()

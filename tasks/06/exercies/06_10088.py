from turtle import *

st = 40
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
ln = st * 8
for x in range(-ln, +ln, st):
    for y in range(-ln, +ln, st):
        setpos(x, y)
        dot(3, 'red')

done()

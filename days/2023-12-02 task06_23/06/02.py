from turtle import *  # pip install turtle


width(1)
color('#0000AA')
lt(90)
st = 30

for _ in range(3):
    fd(10*st)
    rt(120)

up()
for x in range(0, 400, st):
    for y in range(0, 400, st):
        setpos(x, y)
        dot(4, 'red')

done()

from turtle import *

screensize(1000, 1000)
# speed(9)
tracer(0)
m = 30
lt(90)
pd()
for _ in 0,0:
    fd(5*m); lt(90); bk(13*m); lt(90)
pu()
bk(10*m); rt(90); fd(9*m); lt(90)
pd()
for _ in 0,0:
    fd(11*m); rt(90); fd(7*m); rt(90)

pu()
color("red")
for x in range(-0, +22):
    for y in range(-10, +10):
        setpos(x*m, y*m)
        dot(3)

done()  # 14*6 + 12*8 - 10 = 84 + 96 - 10 = 170

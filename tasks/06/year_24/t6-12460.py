from turtle import *

screensize(900, 900)
k = 20
tracer(0)  # speed(9)

for i in range(3):
    pd()
    for j in range(2):
        fd(7*k); rt(90)
        fd(7*k); rt(90)
    pu()
    fd(6*k); rt(90); fd(6*k); lt(90)

for x in range(-5, +22):
    for y in range(-20, +8):
        setpos(x*k, y*k)
        dot(3)
done()

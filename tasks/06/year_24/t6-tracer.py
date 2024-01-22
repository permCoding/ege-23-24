from turtle import *

k = 20
tracer(0)  # speed(9)
pd()
for i in range(24):
    fd(3*k)
    lt(60)
pu()
for x in range(-5, +8):
    for y in range(-5, +8):
        setpos(x*k, y*k)
        dot(3)
done()

from turtle import *

screensize(1200, 1200)

tracer(0)
m = 60
lt(90)
pd()
for _ in range(12):
    fd(4*m); rt(144); fd(4*m); lt(72)

pu()
color("red")
for x in range(-10, +10):
    for y in range(-10, +10):
        setpos(x*m, y*m)
        dot(3)

done()  # 30

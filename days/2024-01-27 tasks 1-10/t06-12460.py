from turtle import *

screensize(1200, 1200)
tracer(0)
m = 30

for i in range(3):
    pd()
    for j in range(2):
        fd(7*m); rt(90); fd(7*m); rt(90)
    pu()
    fd(6*m); rt(90); fd(6*m); lt(90)

pu()
color("red")
for x in range(-25, +20):
    for y in range(-25, +5):
        setpos(x*m, y*m)
        dot(3)

done()  # 28 + 48 = 76

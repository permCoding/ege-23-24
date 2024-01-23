from turtle import *


screensize(1200, 1200)
k = 30
tracer(0)
pd()
for i in range(2):
    fd(5*k) 
    lt(90)
    bk(13*k)
    lt(90)

pu()
bk(10*k); rt(90); fd(9*k); lt(90)

pd()
for i in range(2):
    fd(11*k)
    rt(90)
    fd(7*k)
    rt(90)
dot(5)
pu()
for x in range(-12, +8):
    for y in range(-18, +5):
        setpos(x*k, y*k)
        dot(3)
done()  # 8*12 + 6*9 + 4*5 = 170

"""
Определите, сколько точек с целочисленными координатами будут находиться внутри объединения фигур, ограниченного заданными алгоритмом линиями, включая точки на линиях.
"""
from turtle import *

screensize(900, 900)
tracer(0)
k = 40
width(1)
pd()
for _ in range(12):
    fd(4*k); rt(144); fd(4*k); lt(72)
pu()
color("red")
for x in range(-10, +10):
    for y in range(-10, +10):
        setposition(x*k, y*k)
        dot(3)

done()

"""
Повтори 12 
    Вперёд 4 
    Направо 144 
    Вперёд 4 
    Налево 72
"""

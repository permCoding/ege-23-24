from turtle import *

step = 15  # сколько шагов нужно чтобы фигура замкнулась
color("red")
width(2)
speed(9)

for i in range(step):
    forward(5 * step)
    left(45)
    backward(5 * step)
    right(30)

done()

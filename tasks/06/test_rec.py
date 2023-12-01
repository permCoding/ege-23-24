from turtle import *


def draw(step):
    if step > 1:
        forward(step)
        right(20)
        draw(step-3)


color('green')
width(3)
step = 100
draw(step)

done()

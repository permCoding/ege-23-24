from turtle import *


def draw(step):
    if step > 1:
        t.fd(step)
        t.rt(28)
        draw(step-1)


t = Turtle()
t.up()
t.speed(6)

t.setpos(-250, +250)
t.screen.bgcolor('orange')
t.clear()

t.color('green')
t.width(3)
step = 150

t.down()
draw(step)

done()

from turtle import *

speed(9)
for steps in range(50):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

done()

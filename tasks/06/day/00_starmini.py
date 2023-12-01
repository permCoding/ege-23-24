from turtle import *

step = 15
color("#BB0000")
width(2)
speed(9)

for i in range(24):
    fd(5 * step)
    lt(45)
    back(5 * step)
    rt(30)

done()

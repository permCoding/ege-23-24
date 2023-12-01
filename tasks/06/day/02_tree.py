from turtle import *


def draw(step):
    if step > 15:
        
        fd(step)
        
        rt(angle)
        draw(0.65 * step)
        rt(-angle)
        
        rt(-angle)
        draw(0.65 * step)
        rt(angle)
        
        fd(-step)


width(2)
speed(9)
color('#19581d')
bgcolor('#e9f1e1')
right(-90)
angle = 38

draw(100)

done()

from turtle import *  # pip install turtle


width(3)
color('#0000AA')
lt(90)
st = 30

for _ in 1,2:
    fd(8*st)
    rt(90)
    fd(18*st)
    rt(90)

up()

fd(4*st)
rt(90)
fd(10*st)
lt(90)

down()

for _ in 1,2:
    fd(17*st)
    rt(90)
    fd(7*st)
    rt(90)
    
done()

from turtle import *

st = 50
speed(9)
lt(90)

for i in 1,2,3:
    lt(90)
    for j in 1,2,3,4:    
        fd(5*st)
        rt(90)

penup()
ln = st * 6
for x in range(-ln, +ln, st):
    for y in range(-ln, +ln, st):
        setpos(x, y)
        dot(3, 'red')

done()  # 56

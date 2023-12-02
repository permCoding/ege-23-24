from turtle import *

st = 20
speed(9)
lt(90)  # чтобы смотрела вверх

# начало

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

# конец

penup()
ln = st * 5
for x in range(-0*ln, +4*ln, st):
    for y in range(-0*ln, +5*ln, st):
        setpos(x, y)
        dot(3, 'red')

done()

print(9*19 + 8*18 - 5*8)  # 275
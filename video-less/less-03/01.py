from random import randint as rnd


com = rnd(100, 999)
print(com)

hum = int(input())
if com == hum: print('Угадал')
if com > hum: print('Больше')
if com < hum: print('Меньше')

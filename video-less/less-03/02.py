from random import randint as rnd


com = rnd(100, 999)
print(com)

while True:
    hum = int(input("Сделайте свой ход - "))
    if com == hum: 
        print('Угадал')
        break
    elif com > hum:
        print('Больше')
    else:
        print('Меньше')

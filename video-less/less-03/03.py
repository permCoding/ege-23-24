from random import randint as rnd


com = rnd(100, 999)
print(com)

k = 0
while True:
    k += 1
    hum = int(input(f"Сделайте свой ход {k} - "))
    if com == hum:
        break
    elif com > hum:
        print('Больше')
    else:
        print('Меньше')

print(f'Угадал на шаге - {k}')
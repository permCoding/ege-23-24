from random import randint as rnd


com = rnd(100, 999)
print(com)

k, s = 0, 1_000
while True:
    k += 1; s -= 100
    hum = int(input(f"Сделайте свой ход №{k} - "))
    print(f"Осталось - {s}")
    if com == hum:
        break
    elif com > hum:
        print('Больше')
    else:
        print('Меньше')

print(f'Угадал на шаге - {k}')
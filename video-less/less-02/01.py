from random import randint


print('0 - Камень\n1 - Ножницы\n2 - Бумага')
res = [0, 0]
while res[0] < 3 and res[1] < 3:
    com = str(randint(0, 2))
    hum = input('Сделайте свой ход - ')

    if hum+com in ['01', '12', '20']:
        res[0] += 1
    if hum+com in ['10', '21', '02']:
        res[1] += 1
    print(f'hum = {res[0]}; com = {res[1]}')

print("Победил" if res[0] > res[1] else "Проиграл")

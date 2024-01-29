from random import randint


lst = ['Камень', 'Ножницы', 'Бумага']  # 0 1 2

com = str(randint(0, 2))
print('Камень - 0, Ножницы - 1, Бумага - 2')
hum = input('Сделайте свой ход - ')

print(hum, com)

if hum == com:
    print('Ничья')
elif hum+com in ['01', '12', '20']:
    print('Победа')
else:
    print('Проигрыш')
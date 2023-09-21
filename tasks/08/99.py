# https://inf-ege.sdamgia.ru/problem?id=10500
k = 0
for i in range(10000, 55555):
    s = str(i)
    if '6' in s or '7' in s or '8' in s or '9' in s or '0' in s:
        continue
    if s.count('1') != 3:
        continue
    k += 1
print(k)

'''
Шифр кодового замка представляет собой последовательность из пяти символов, 
каждый из которых является цифрой от 1 до 5. Сколько различных вариантов шифра 
можно задать, если известно, что цифра 1 встречается ровно три раза, а каждая 
из других допустимых цифр может встречаться в шифре любое количество раз или 
не встречаться совсем?
Ответ: 160
'''


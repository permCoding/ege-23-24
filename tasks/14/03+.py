# https://inf-ege.sdamgia.ru/problem?id=27545

n = 49**7 * 7**20 - 7**8 - 28

cnt = 0
while n > 0:
    if n%7==6: cnt += 1
    n //= 7
print(cnt)

'''
Значение выражения 49**7 * 7**20 - 7**8 - 28 
записали в системе счисления с основанием 7. 
Сколько цифр 6 содержится в этой записи?
'''
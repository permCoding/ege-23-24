from re import search
from fnmatch import fnmatch
# https://inf-ege.sdamgia.ru/problem?id=57432


def check1(s):  # h = '12??1*56'
    if len(s)<7: return False
    return s[:2]=='12' and s[4]=='1' and s[-2:]=='56'

def check2(s):  # h = '12??1*56'
    return search('^12..1.*56$', s)

def check3(s):  # h = '12??1*56'
    return fnmatch(s, '12??1*56')

n, d = 0, 317
while n < 100_000_000:
    n += d
    if check3(str(n)): print(n, n//d)

"""
Среди натуральных чисел, не превышающих 10**8, 
найдите все числа, соответствующие маске 12??1*56, 
делящиеся на 317 без остатка.

В ответе запишите в первом столбце таблицы все найденные числа
в порядке возрастания, а во втором столбце — 
соответствующие им результаты деления этих чисел на 317.
"""
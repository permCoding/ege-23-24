from fnmatch import *
import re
# https://inf-ege.sdamgia.ru/problem?id=61405

def f1():
    for n in range(2024, 10**10+1, 2024):
        s = str(n)  # '3?2258*4'
        if s[0]=='3' and s[2:6]=='2258' and s[-1]=='4':
            print(n)

def f2():
    n = 2024
    while n < 10**10:
        s = str(n)  # '3?2258*4'
        if s[0]=='3' and s[2:6]=='2258' and s[-1]=='4':
            print(n)
        n += 2024

def f3():  # '3?2258*4'
    # p = '^3.2258.*4$'
    p = '^3\d2258\d*4$'
    for n in range(2024, 10**10+1, 2024):
        if re.search(p, str(n)):
            print(n)

def f4():  # '3?2258*4'
    p = re.compile('^3\d2258\d*4$')
    for n in range(2024, 10**10+1, 2024):
        if p.search(str(n)):
            print(n)

def f5():
    for x in range(2024, 10**10, 2024): 
        if fnmatch(str(x), '3?2258*4'):
            print(x)

f4()

"""
Найдите все натуральные числа, не превышающие 10**10, 
которые соответствуют маске 3?2258*4 
и при этом без остатка делятся на 2024.

В ответе запишите все найденные числа в порядке возрастания.

"""
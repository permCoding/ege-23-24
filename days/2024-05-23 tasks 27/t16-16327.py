import sys
sys.set_int_max_str_digits(0)
sys.setrecursionlimit(4_000)

def f1(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

def f2(n):
    if n == 1:
        return 1
    else:
        return n * f2(n-1)

x = f1(2024)/f1(2022)
y = f1(2023)/f1(2022)
print(x, y, x-y)
x = f2(2024)/f2(2022)
y = f2(2023)/f2(2022)
print(x, y, x-y)

"""
(2024! - 2023!) / 2022!

2024!/2022!  -  2023!/2022!

a - b = ? = 2023*(2024 - 1) = 2023**2 = 4092529

a = 1*2*3*..*2022*2023*2024/1*2*3*..*2022
a = 2023*2024
b = 2023

"""
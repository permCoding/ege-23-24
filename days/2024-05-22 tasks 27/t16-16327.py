import sys
sys.set_int_max_str_digits(0)
sys.setrecursionlimit(12_000)
def f1(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

def f2():
    pass

x = f1(2024)/f1(2022)
y = f1(2023)/f1(2022)
print(x, y, x-y)

"""
(2024! - 2023!) / 2022!

2024!/2022!  -  2023!/2022!

a - b = ? = 2023*(2024 - 1) = 2023**2 = 4092529

a = 1*2*3*..*2022*2023*2024/1*2*3*..*2022
a = 2023*2024
b = 2023

"""
def d(n, m): return n%m == 0

def f(x, A):
    arg1 = not(d(x,A)) and d(x,35)
    arg2 = not(d(x,21)) or not(d(x,35))
    return arg1 <= arg2

for A in range(300, 0, -1):
    if all(f(x, A) for x in range(500)):
        print(A)
        break

"""
a b ->  <=
0 0 1
0 1 1
1 0 0
1 1 1
"""
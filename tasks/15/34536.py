from itertools import *

def f(x, l, r):
    xA = l <= x <= r
    xP = 5 <= x <= 15
    xQ= 10 <= x <= 20
    return xP and xQ or xA

k = 10
Ox = [i/k for i in range(4*k, 21*k+1)]

mn = []
for l,r in combinations(Ox, 2):
    print(l,r)
    # if all(f(x, l, r) for x in Ox):
    #     mn.append(r-l)
print(mn)

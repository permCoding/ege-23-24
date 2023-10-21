# import sys


def get(n):
    if n == 0:  # точка останова
        print(n)
    else:  # шаг рекурсии
        print(n)
        get(n-1)


n = int(input())
get(n)

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(20000)

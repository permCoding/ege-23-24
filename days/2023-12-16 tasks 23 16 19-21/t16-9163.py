from functools import lru_cache
import sys


@lru_cache
def f(n):
    if n >= 2025: return n
    return f(n+1) - f(n+2) + 7


sys.setrecursionlimit(24000)
print(f(15) - f(24))

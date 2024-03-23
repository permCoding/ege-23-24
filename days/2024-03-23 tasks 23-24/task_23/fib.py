def fib_1(n):
    if n < 3: return 1
    return fib_1(n-2) + fib_1(n-1)


from functools import lru_cache
@lru_cache()
def fib_2(n):
    if n < 3: return 1
    return fib_2(n-2) + fib_2(n-1)


def fib_3(n):
    if n < 3: return 1
    if cache[n-2] == 0: cache[n-2] = fib_3(n-2)
    if cache[n-1] == 0: cache[n-1] = fib_3(n-1)
    return cache[n-2] + cache[n-1]


def fib_4(n):
    cache = [0,1,1]
    for num in range(3, n):
        cache.append(cache[-2]+cache[-1])
    print(cache, cache[-1])


n = 36
cache = [0,1,1] + [0] * n
print(fib_3(n))
print(cache)
fib_4(n)
'''
0 1 2 3 4 5 6  7  8  9 10
0 1 1 2 3 5 8 13 21 34 55
'''
def get_for(n):
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, a + b
    return a, b

def get(n):
    if n < 3: return 1
    return get(n-1) + get(n-2)


def get_cache(n):    
    if n < 3: return 1
    if cache[n-1] == 0: cache[n-1] = get_cache(n-1)
    # if cache[n-2] == 0: cache[n-2] = get_cache(n-2)
    return cache[n-1] + cache[n-2]


num = 35
print(get_for(num))
print(get(num))
cache = [0,1,1] + [0] * num
print(get_cache(num))


# 1 2 3 4 5 6
# 1 1 2 3 5 8 
#       a b
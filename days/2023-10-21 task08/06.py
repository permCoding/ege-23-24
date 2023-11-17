def algo(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + '0101'
    else:
        b = '1' + b
    return int(b, 2)


def get(g):
    mn = 99999999  # float("inf")
    for n in range(1, 1024):
        r = algo(n)
        if r > g:
            if r < mn:
                mn = r
    return mn


g = int(input())
print(get(g))

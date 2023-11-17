def algo(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + '0101'
    else:
        b = '1' + b
    return int(b, 2)


def get(g):
    t = []
    for n in range(1, 1024):
        r = algo(n)
        if r > g:
            t.append(r)
    return min(t)


g = int(input())
print(get(g))

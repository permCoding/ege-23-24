def algo(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + '0101'
    else:
        b = '1' + b
    return int(b, 2)


def get(g):
    return min([algo(n) for n in range(1, 1024) if algo(n) > g])


g = int(input())
print(get(g))

def algo(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    return int(b, 2)


def find(g):
    t = []  # list
    for n in range(1, 1500):
        r = algo(n)
        if r > g:
            t.append(r)
    return min(t)


g = int(input())
print(find(g))


##tpl = (1, 3, 4)  # tuple





"""
i = 9
while i >= 0:
    print(i)
    i -= 1  # i = i + 1
"""

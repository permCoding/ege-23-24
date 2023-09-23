t = []  # list
for n in range(1, 500):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)

    if r > 151:
        t.append(r)

print(min(t))

tpl = (1, 3, 4)  # tuple





"""
i = 9
while i >= 0:
    print(i)
    i -= 1  # i = i + 1
"""

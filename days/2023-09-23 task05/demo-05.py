mn = 8888888888888888888
for n in range(1, 500):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)

    if r > 151 and r < mn:
        mn = r

print(mn)




"""
i = 9
while i >= 0:
    print(i)
    i -= 1  # i = i + 1
"""

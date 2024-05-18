mn = 2**30
for n in range(1, 10_000):
    b = bin(n)[2:]
    b += bin((n%3)*3)[2:] if n%3 else b[-2:]
    r = int(b,2)
    if r >= 195 and r < mn:
        mn = r
print(mn)

t = []
for n in range(1, 10_000):
    b = bin(n)[2:]
    b += bin((n%3)*3)[2:] if n%3 else b[-2:]
    r = int(b,2)
    if r >= 195: t += [r]
print(min(t))
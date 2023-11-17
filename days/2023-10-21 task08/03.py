# g = int(input())
g = 9

t = []
for n in range(1, 1024):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + '0101'
    else:
        b = '1' + b
    r = int(b, 2)
    if r > g:
        t.append(r)

print(min(t))

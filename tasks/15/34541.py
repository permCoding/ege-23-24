def f(x):
    xP =  30 <= x <= 380
    xQ = 210 <= x <= 570
    return int(int(xQ) <= int(xP)) <= 0

mx = 0
for l in range(0, +590):
    for r in range(l+10, +600):
        if all(f(x) for x in range(l, r+1)):
            mx = max(mx, r-l)
print(mx/10)

def f(x):
    xP = 2 <= x <=10
    xQ = 6 <= x <=14
    return (1 <= int(xP)) or xQ

mx = 0
for l in range(-5, +19):
    for r in range(l+1, +20):
        if all(f(x) for x in range(l, r+1)):
            print(l, r, r-l)
            mx = max(mx, r-l)
print(mx)

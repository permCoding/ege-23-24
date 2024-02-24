def f(a, b):
    return int(a)%2 != int(b)%2
k = 0
for n in range(10_000, 100_000):
    s = str(n)
    if len(set(s)) == 5:
        if f(s[0],s[1]) and f(s[1],s[2]) and f(s[2],s[3]) and f(s[3],s[4]):
            k += 1
print(k)
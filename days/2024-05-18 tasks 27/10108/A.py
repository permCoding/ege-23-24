f = open('./27_A_10108.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mx_sm = -2**30
for a in range(0, n-2*k):
    for b in range(a+k, n-k):
        for c in range(b+k, n):
            mx_sm = max(mx_sm, t[a]+t[b]+t[c])
print(mx_sm)

f = open('./27-A.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mx_abc = -float('inf')
for a in range(0, n-2*k):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            if b-a == 2*k or c-b == 2*k or c-a == 2*k:
                mx_abc = max(mx_abc, t[a]+t[b]+t[c])
print(mx_abc)  # 205706  23894.

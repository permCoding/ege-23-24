f = open('./27_A_10108.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mx_sm = -3*10**7  # -float('inf') 
mx_a = -10**7  # -float('inf') 
for b in range(k, n):
    a = b - k
    mx_a = max(mx_a, t[a])
    mx_sm = max(mx_sm, mx_a + t[b])
print(mx_sm)

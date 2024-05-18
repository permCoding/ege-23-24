f = open('./27_B_10108.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mx_a = -10**7  # -float('inf') 
mx_ab = -2*10**7  # -float('inf') 
mx_abc = -3*10**7  # -float('inf') 

for c in range(2*k, n):  # a b c
    a, b = c - 2*k, c - k
    mx_a = max(mx_a, t[a])
    mx_ab = max(mx_ab, mx_a + t[b])
    mx_abc = max(mx_abc, mx_ab + t[c])

print(mx_abc)

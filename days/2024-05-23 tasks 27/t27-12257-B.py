# f = open('./12257-T.txt')
f = open('./12257-A.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

# K = 5_000  # T
K = 113  # A B

s = [0] * n
p = [2**30] * K
for i in range(n):
    s[i] = s[i-1] + t[i]
    pos = s[i]%K
    p[pos] = min(p[pos], s[i])

mx_sm = 0
for i in range(n):
    pos = s[i]%K
    sm = s[i]-p[pos]
    mx_sm = max(mx_sm, sm)
print(mx_sm)  # A=980 B=4999984
"""
выбрать непрерывн подпоследовательности 
с максимальной суммой, кратной К

из них выбрать самую длинную
"""
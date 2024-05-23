# f = open('./12257-T.txt')
f = open('./12257-A.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

# K = 5_000  # T
K = 113  # A B

mx_sm = 0
mx_ln = 0
for a in range(n):
    for b in range(a, n):
        sm = sum(t[a:b+1])
        if sm%K==0 and sm >= mx_sm:
                mx_sm = sm
                mx_ln = max(mx_ln, b-a+1)
print(mx_sm, mx_ln)  # A=980 B=4999984
"""
выбрать непрерывн подпоследовательности 
с максимальной суммой, кратной К

из них выбрать самую длинную
"""
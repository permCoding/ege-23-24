from math import ceil
f = open('./7275-B.txt')
n, m = map(int, f.readline().split())

t = [0] * 10**7  # max index+1

for _ in range(n):
    i, p = map(int, f.readline().split())
    t[i] = ceil(p/30)  # A B

sm, sm_mx = sum(t[0:2*m+1]), 0
if t[m] != 0: sm_mx = sm

for i in range(m+1, len(t)-m):
    sm += t[i+m] - t[i-m-1]
    if t[i] != 0: sm_mx = max(sm_mx, sm)
print(sm_mx)  # A=264 B=27140

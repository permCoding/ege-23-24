from math import ceil
f = open('./7275-A.txt')
n, m = map(int, f.readline().split())

t = [0] * 10**3  # max index+1

for _ in range(n):
    i, p = map(int, f.readline().split())
    # t[i] = ceil(p/96)  # T
    t[i] = ceil(p/30)  # A

sm_mx = 0
for i in range(m, len(t)-m):
    if t[i] != 0:
        sm = sum(t[i-m:i+m+1])
        sm_mx = max(sm_mx, sm)
print(sm_mx)  # A=264 B=27140


"""

"""
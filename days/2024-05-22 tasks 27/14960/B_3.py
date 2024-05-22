# f = open('./27_A_14960.txt')
f = open('./T.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
r = [t[i]-t[i-1] for i in range(1, n)]

sm_pr = [0]
for elm in r: sm_pr.append(sm_pr[-1] + elm)

pr_mn = [0]
for ind in range(1, len(sm_pr)):
    pr_mn += [ sm_pr[ind] if sm_pr[ind] < pr_mn[-1] else pr_mn[-1] ]

sm_mx = -2**30
for i in range(1, len(sm_pr)):
    sm_mx = max(sm_mx, sm_pr[i] - pr_mn[i-1])

print(sm_mx)

# A=150 B=360685
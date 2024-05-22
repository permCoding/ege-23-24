f = open('./27_B_14960.txt')
# f = open('./T.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
r = [t[i]-t[i-1] for i in range(1, n)]

sm_pr = [0]
for elm in r: sm_pr.append(sm_pr[-1] + elm)

pr_mn = [ (0, 0) ]  # sm, ind
for ind in range(1, len(sm_pr)):
    pr_mn += [ (sm_pr[ind],ind) if sm_pr[ind] <= pr_mn[-1][0] else pr_mn[-1] ]
# print(pr_mn)

sm_mx, ln = -2**30, 0
for i in range(1, len(sm_pr)):
    if sm_pr[i] - pr_mn[i-1][0] >= sm_mx:
        sm_mx = sm_pr[i] - pr_mn[i-1][0]
        ln = i - pr_mn[i-1][1]

print(sm_mx, ln+1)

# A=150 B=360685
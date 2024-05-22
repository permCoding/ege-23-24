# f = open('./27_A_14960.txt')
f = open('./T.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
r = [t[i]-t[i-1] for i in range(1, n)]

sm_pr = [0]
for elm in r: sm_pr.append(sm_pr[-1] + elm)

pr_mn = [0]
for ind in range(1, len(sm_pr)):
    # if sm_pr[ind] < pr_mn[-1]:
    #     pr_mn.append( sm_pr[ind] )
    # else:
    #     pr_mn.append( pr_mn[-1] )
    pr_mn += [ sm_pr[ind] if sm_pr[ind] < pr_mn[-1] else pr_mn[-1] ]

print(pr_mn)
    # print(sm_pr[ind] - mn_pr + 1)

# A=150 B=360685
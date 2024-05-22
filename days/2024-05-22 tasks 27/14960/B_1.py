f = open('./27_A_14960.txt')
# f = open('./T.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
r = [t[i]-t[i-1] for i in range(1, n)]

sm_pr = [0]
for elm in r: sm_pr.append(sm_pr[-1] + elm)

for ind in range(1, len(sm_pr)):
    mn_pr = min(sm_pr[0: ind])
    print(sm_pr[ind] - mn_pr + 1)
# print(sm_mx, ln_mn+1)

# A=150 B=360685
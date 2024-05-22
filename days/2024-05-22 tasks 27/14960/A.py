f = open('./27_A_14960.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
r = [t[i]-t[i-1] for i in range(1, n)]

sm_mx, ln_mn = -2**30, 2**30
for lt in range(0, n):
    for rt in range(lt, n):
        sm = sum(r[lt:rt+1])
        if sm >= sm_mx:
            sm_mx = sm
            ln_mn = rt - lt + 1
print(sm_mx, ln_mn+1)  # 9939

# A=150 B=360685
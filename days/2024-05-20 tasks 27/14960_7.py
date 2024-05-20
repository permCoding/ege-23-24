# f = open('./T.txt')
f = open('./27_A_14960.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
p = [t[i]-t[i-1] for i in range(1, n)]
# p = [-5, 0, 5, -2, 2, -6, -1]

mx_sm = -10_000  # -float('inf')
mn_ln = 10**7
for lt in range(0, len(p)):
    sm = 0
    for rt in range(lt, len(p)):
        sm += p[rt]
        if sm >= mx_sm:
            mx_sm = sm
            mn_ln = rt - lt +1 +1

print(mx_sm, mn_ln)


# print(mx_rt - mx_lt + 1 + 1)

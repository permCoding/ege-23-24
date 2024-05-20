# f = open('./T.txt')
f = open('./27_A_14960.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
p = [t[i]-t[i-1] for i in range(1, n)]
# p = [-5, 0, 5, -2, 2, -6, -1]

subs = []
for lt in range(0, len(p)):
    sm = 0
    for rt in range(lt, len(p)):
        sm += p[rt]
        subs += [ (sm, lt, rt) ]

mx_sm = max(subs, key=lambda x: x[0])[0]
# print(mx_sm)

subs = list(filter(lambda x: x[0] == mx_sm, subs))
# print(subs, len(subs))

mx_rt = max(subs, key=lambda x: x[2])[2]
# print(mx_rt)

subs = list(filter(lambda x: x[2] == mx_rt, subs))
# print(subs)

mx_lt = max(subs, key=lambda x: x[1])[1]

print(mx_rt - mx_lt + 1 + 1)

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
        subs += [ (sm, rt, lt) ]

subs.sort()
for sub in subs[-100:]: print(sub)

print( subs[-1][1] - subs[-1][2] +1 +1 )

# rt - lt + 1 + 1

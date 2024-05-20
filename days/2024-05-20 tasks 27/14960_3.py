# f = open('./T.txt')
f = open('./27_A_14960.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
p = [t[i]-t[i-1] for i in range(1, n)]
# p = [-5, 0, 5, -2, 2, -6, -1]
# print(p)

subs = []
for lt in range(0, len(p)):
    sm = 0
    for rt in range(lt, len(p)):
        sm += p[rt]
        subs += [ (sm, lt, rt) ]

for tpl in subs[-200:]:
    print( tpl )

# rt - lt + 1 + 1

# f = open('./T.txt')
# n = int(f.readline())
# t = [int(f.readline()) for _ in range(n)]
# p = [t[i]-t[i-1] for i in range(1, n)]
p = [-5, 0, 5, -2, 2, -6, -1]
# print(p)

subs = []
for lt in range(0, len(p)):
    sm = 0
    for rt in range(lt, len(p)):
        sm += p[rt]
        subs += [ sm ]

print( max(subs) )

# f = open('./T.txt')
# n = int(f.readline())
# t = [int(f.readline()) for _ in range(n)]
# p = [t[i]-t[i-1] for i in range(1, n)]
p = [-5, 0, 5, -2, 2, -6, -1]
# print(p)

subs = []
for lt in range(0, len(p)):
    for rt in range(lt, len(p)):
        # subs += [ sum(p[lt:rt+1]) ]
        subs.append( sum(p[lt:rt+1]) )

print( max(subs) )

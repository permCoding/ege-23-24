# f = open('./27_A_14960.txt')
f = open('./T.txt')
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]
r = [t[i]-t[i-1] for i in range(1, n)]

# sm_pr = [0]
# for elm in r:
#     sm_pr.append(sm_pr[-1] + elm)
sm, sm_pr = 0, [0]
for i in range(len(r)):
    sm += r[i]
    sm_pr += [ sm ]
print(sm_pr)



# print(sm_mx, ln_mn+1)

# A=150 B=360685
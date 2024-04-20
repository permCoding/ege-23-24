f = open('./data/26_10107.txt')
n = int(f.readline())
pairs = sorted(
    [tuple(map(int, line.split())) for line in f],
    key=lambda x: x[1]
)

res = [pairs[0]]
last_ind = 0
for i in range(1, n):
    if pairs[i][0] >= res[-1][1]:
        res.append( pairs[i] )
        last_ind = i

dif = res[-1][0]-res[-2][1]
for elm in pairs[last_ind+1:]:
    dif = max(dif, elm[0]-res[-2][1])

print(len(res), dif)

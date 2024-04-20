f = open('./data/test_14595.txt')
n = int(f.readline())
pairs = sorted(
    [tuple(map(int, line.split())) for line in f],
    key=lambda x: x[1]
)

res = [pairs[0]]
last_ind = 0
cnt = 0
for i in range(1, n):
    # shift = 10 if cnt%3 == 0 else 0
    # if pairs[i][0] >= res[-1][1] + shift:
    if pairs[i][0] >= res[-1][1] + [10,0,0][cnt%3]:
        res.append( pairs[i] )
        last_ind = i
        cnt += 1

print(pairs)
print(res)

dif = res[-1][0]-res[-2][1]
for elm in pairs[last_ind+1:]:
    dif = max(dif, elm[0]-res[-2][1])

print(len(res), dif)

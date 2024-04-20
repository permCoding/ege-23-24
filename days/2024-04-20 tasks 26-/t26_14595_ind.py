f = open('./data/test_14595.txt')
n = int(f.readline())
pairs = sorted(
    [tuple(map(int, line.split())) for line in f],
    key=lambda x: x[1]
)

cnt, fin, last_ind = 0, 0, 0
for i in range(0, n):
    if pairs[i][0] >= fin:
        cnt += 1
        fin = pairs[i][1]
        last_ind = i
        if cnt%3 == 0: fin += 10

print(cnt)

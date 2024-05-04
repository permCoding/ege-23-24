# f = open('./data/test_14595.txt')
f = open('./data/26_14595.txt')
n = int(f.readline())
pairs = sorted(
    [tuple(map(int, line.split())) for line in f],
    key=lambda x: x[1]
)

cnt = 1
prev = 0  # последняя взятая лекция
for i in range(1, n):
    shift = 10 if cnt%3 == 0 else 0
    if pairs[i][0] >= pairs[prev][1] + shift:
        if shift: last = (prev, i, cnt)
        cnt += 1
        prev = i

print(cnt, last)
a, b = last[0], last[1]
print(pairs[b][0], pairs[a][1])

srt = sorted(filter(lambda x: x[0]>=pairs[a][1], pairs[b:]))

for pair in srt: print(pair)
# 26 36
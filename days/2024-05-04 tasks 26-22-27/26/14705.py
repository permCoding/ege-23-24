# f = open('./data/test_14705.txt')
f = open('./data/26_14705.txt')
n = int(f.readline())
pairs = [list(map(int, line.split())) for line in f]

t = [0] * 5_000_000
for a, b in pairs:
    t[a] += 1
    t[b] -= 1

for i in range(1, len(t)): t[i] += t[i-1]
max_count = max(t)

max_len = cur_len = 0
for elm in t:
    if elm == max_count:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_count, max_len)

# import re
# s = ''.join(map(str, t))
# s = re.sub(str(max_count), '#', s)
# for elm in re.findall('#+', s):
#     print(len(elm))
# print(max_count)

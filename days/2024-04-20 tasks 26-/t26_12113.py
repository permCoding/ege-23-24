dif = 7
f = open('./data/26_12113.txt')
n = int(f.readline())
t = [int(line) for line in f]
# t = [43, 40, 33, 28, 40, 29]  # dif = 3
# t = [28, 29, 32, 35]  # dif = 3

t.sort()

res = [t[0]]
for elm in t:
    if elm%2 != res[-1]%2 and elm - res[-1] >= dif:
        res += [elm]
print(len(res), res[0])

for start in range(0, n):
    if t[0]%2 != t[start]%2:
        break

res = [t[start]]
for elm in t[start+1:]:
    if elm%2 != res[-1]%2 and elm - res[-1] >= dif:
        res += [elm]
    
print(len(res), res[0])
"""
dif = 3
28 29 32 35 => 28 35 => 2 28
28 29 32 35 => 29 32 35 => 3 29
"""
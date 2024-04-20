f = open('./data/26_13397.txt')
n = int(f.readline())
pairs = []
for line in f:
    a, b = map(int, line.split())
    pairs.append( (a, a+b) )
    
pairs.sort(key=lambda pair: pair[1])

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

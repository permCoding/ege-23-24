f = open('./data/test_13397.txt')
n = int(f.readline())
pairs = []
for line in f:
    a, b = map(int, line.split())
    pairs.append( (a, a+b) )
    
pairs.sort(key=lambda pair: pair[1])

fin, cnt = 0, 0
for pair in pairs:
    if pair[0] >= fin:
        print(pair)
        fin = pair[1]
        cnt += 1

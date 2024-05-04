f = open('./26-15337.txt')
t = []
for line in f:
    a,b,c = line.split('\t')
    t.append( [int(a),int(b),list(map(int, c.split(';')))] )

pairs = [ [0, 0] ] * (len(t)+1) # начало конец
for elm in t:
    fin = max(pairs[i][1] for i in elm[2])
    pairs[elm[0]] = [fin, fin + elm[1]]

for i, pair in enumerate(pairs): print(i, pair)

max_value = max(pairs, key=lambda x: x[1])[1]
t = [0] * (max_value+1)
for a, b in pairs:
    t[a] += 1
    t[b] -= 1

for i in range(1, len(t)): t[i] += t[i-1]
print(t)
max_count = max(t)

max_len = cur_len = 0
for elm in t:
    if elm == max_count:  # 5
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_count, max_len) 
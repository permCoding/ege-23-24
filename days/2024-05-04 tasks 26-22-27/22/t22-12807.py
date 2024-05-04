# f = open('./test-26-12807.txt')
f = open('./26-12807.txt')
t = []
for line in f:
    a,b,c = line.split('\t')
    t.append( [int(a),int(b),list(map(int, c.split(';')))] )

pairs = [ [0, 0] ] * (len(t)+1) # начало конец
for elm in t:
    fin = max(pairs[i][1] for i in elm[2])
    pairs[elm[0]] = [fin, fin + elm[1]]

print(max(pairs, key=lambda x: x[1]))

# for i, pair in enumerate(pairs): print(i, pair)
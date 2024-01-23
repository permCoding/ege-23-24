k = 0
for s in open('./t9_12241.csv'):
    p = list(map(int, s.split(',')))
    t = set(p)
    if len(t) == 4 and all(p.count(e)<3 for e in t):
        m = [e for e in t if p.count(e)==2]
        if (min(m)+max(m))/2 < (sum(t)-sum(m)):
            k += 1
print(k)  # 3382
        
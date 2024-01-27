k = 0
for line in open('./09_12241.csv'):
    t = [int(e) for e in line.split(',')]
    p = [e for e in t if t.count(e) == 2]
    if len(p) == 6:
        if (min(p) + max(p))/2 < sum(t) - sum(p):
            k += 1
print(k)  # 3382

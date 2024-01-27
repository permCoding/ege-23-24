sm, temp = 0, '35555'
for r in range(10_000-4):
    s = temp + '5'*r
    while s.find('333') >= 0 or s.find('555') >= 0:
        if s.find('555') >= 0:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)
    sm = max(sm, sum(int(e) for e in s))
    print(sm)
print(sm)  # 26

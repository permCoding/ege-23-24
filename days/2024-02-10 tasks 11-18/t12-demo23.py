for n in range(9_000, 10_000):
    l: str = '5' + '2' * n
    while ('52' in l) or ('2222' in l) or ('1122' in l):
        l = l.replace('52', '11', 1)
        l = l.replace('2222', '5', 1)
        l = l.replace('1122', '25', 1)
    if sum(int(s) for s in l) == 64: 
        print(n)
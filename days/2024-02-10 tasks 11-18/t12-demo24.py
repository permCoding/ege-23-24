def is_prime(n):
    for d in range(2, n):
        if n%d == 0:
            return False
    return True


for n in range(300):
    l = '>' + '0' * 39 + '1' * n + '2' * 39
    while ('>1' in l) or ('>2' in l) or ('>0' in l):
        l = l.replace('>1', '22>', 1)
        l = l.replace('>2', '2>', 1)
        l = l.replace('>0', '1>', 1)
    sm = sum(int(s) for s in l if s!='>')
    if is_prime(sm):
        print(sm, n)
        break
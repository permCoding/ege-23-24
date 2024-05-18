def a():
    from itertools import product
    alph = '0123456'
    even = '0246'
    amount = 0
    for tpl in product(alph, repeat=7):
        if tpl[0] == '0': continue
        if len([1 for elm in tpl if elm in even]) == 2:
            amount += 1
    print(amount)


def b():
    def to_seven(n):
        res = ''
        while n > 0:
            res += str(n%7)
            n //= 7
        return res[::-1]
    
    amount = 0
    for n in range(0, 10**7):  # 6666666
        s = to_seven(n)  # n => seven
        if len(s) < 7: continue
        if len(s) > 7: break
        even = 0
        for ch in s: even += (1-int(ch, 7)%2)
        if even == 2: amount += 1
    print(amount)


a()
b()

"""
7
7
2 even
"""
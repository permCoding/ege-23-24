# жадный алгоритм ...
def solver_greedy():
    money.sort()  # print(money)
    right, sm = 0, 0
    while right < len(money):
        if sm + money[right] <= limit:
            sm += money[right]
        else:
            break
        right += 1
    return right

def solver_bin():
    """ метод бинарных масок """
    n = len(money)
    max_cnt = 0
    for n in range(0, 2**n):
        
        sm, cnt, mask = 0, 0, 1
        for i in range(n):
            if n & mask > 0:
                sm += money[i]
                cnt += 1
            mask <<= 1  # mask *= 2
        
        if sm <= limit and cnt > max_cnt:
            max_cnt = cnt
    return max_cnt


def solver_using_bin():
    """ метод через перевод в дв предст числа """
    n = len(money)
    max_cnt = 0
    for n in range(0, 2**n):
        
        sm = 0
        b = bin(n)[2:][::-1]  # ____101
        for i in range(len(b)):
            sm += int(b[i]) * money[i]
        cnt = b.count('1')
        
        if sm <= limit and cnt > max_cnt:
            max_cnt = cnt
    return max_cnt


limit = 1000
money = [2,1,3,5,6,4,9]

print(solver_bin())
print(solver_using_bin())
print(solver_greedy())

"""
n = 
n * log(n) < < 2**n
n**2 < 2**n

2**7
2 1 3 4 6 5 9

0 0 0 0 0 0 0
. . . 
0 0 0 1 0 0 1 (2) == 9
0 0 0 0 0 0 1 (2) == 1 <== mask (10)
0 0 0 0 0 1 0 (2) == 2 <== mask (10)
0 0 0 0 1 0 0 (2) == 4 <== mask (10)

1 0 1 1 0 1 1 (2) <== n (10)

1 1 1 1 1 1 0
1 1 1 1 1 1 1
"""

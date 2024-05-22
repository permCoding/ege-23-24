lines = open('./t09_16320.csv').readlines()
t = [list(map(int,line.split(','))) for line in lines]
cnt = 0
for x in t:
    a = max(x) < sum(x) - max(x)
    p1 = x[0]+x[1] == x[2]+x[3]
    p2 = x[0]+x[2] == x[1]+x[3]
    p3 = x[0]+x[3] == x[2]+x[1]
    b = p1 or p2 or p3
    # x.sort()
    # b = x[0]+x[3] == x[1]+x[2]
    if a and b:
        cnt += 1
print(cnt)
"""
20:07
количество строк таблицы: 
– наибольшее из четырёх чисел меньше суммы трёх других; 
– четыре числа можно разбить на две пары чисел с равными суммами.
"""
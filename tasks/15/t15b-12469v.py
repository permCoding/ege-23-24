from itertools import combinations

def check(x, a):
    d = 7 <= x <= 68
    c = 29 <= x <= 100
    _a = a[0] <= x <= a[1]
    return d <= (((not c) and (not _a)) <= (not d))

res = 999
all_x = [i/4 for i in range(0, 410)]
for a in combinations(all_x, 2):
    if all(check(x, a) for x in all_x):
        res = min(res, a[1]-a[0])
print(res)

"""
Из максимального числа вычитаем минимальное: 
28.75 - 7 = 21.75 и округляем вверх: 21.75 -> 22

На числовой прямой даны два отрезка: D = [7; 68] и C = [29; 100]. Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение
(x∈D)→((¬(x∈C)∧¬(x∈A))→¬(x∈D))
истинно (т.е. принимает значение 1) при любом значении переменной х.
"""

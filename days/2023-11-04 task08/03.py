from itertools import product

count = 0
for item in product("0123", repeat=4):
    if item[0] != '0':
        if  len(set(item)) < 4:
            count += 1
print(count)

lst = []
for item in product("0123", repeat=4):
    if item[0] != '0':
        if  len(set(item)) < 4:
            lst.append(item)
print(len(lst))

"""
https://education.yandex.ru/ege/tasks?task_id=bf1652f7-66e0-45e2-8165-734057cc59db&category_id=6320a497-50f1-4607-be84-efe14accbae6
Сколько существует 4-разрядных четверичных чисел, 
в которых хотя бы одна цифра встречается не менее двух раз?
0032
"""
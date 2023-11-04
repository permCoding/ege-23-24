for d in range(0o1000, 0o10000):
    print(oct(d)[2:])






"""
https://education.yandex.ru/ege/tasks?task_id=bf1652f7-66e0-45e2-8165-734057cc59db&category_id=6320a497-50f1-4607-be84-efe14accbae6
Сколько существует 4-разрядных четверичных чисел, 
в которых хотя бы одна цифра встречается не менее двух раз?
0032 - не начинается с 0
174 - ответ
"""
# def product(lst, repeat):
#     if (repeat == 1): return [*lst]
#     return [(i, *it) for i in lst for it in product(lst, repeat - 1)]
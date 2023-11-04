def to_base(dec, base=4):
    result = ""
    while dec > 0:
        result = str(dec%base) + result
        dec //=base
    return result


# print(to_base(4))
count = 0
for d in range(999999):
    x = to_base(d, 4)
    if len(x) == 4 and x[0] != '0':
        if len(set(x)) < len(x):
            count += 1
print(count)


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
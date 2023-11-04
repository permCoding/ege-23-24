def gen(al, rep, s=""):
    if len(s) == rep:
        return 1
    else:
        count = 0
        for elm in al:
            count += gen(al, rep, s+elm)
        return count


al, rep = "0123", 4
print(gen(al, rep))

"""
https://education.yandex.ru/ege/tasks?task_id=bf1652f7-66e0-45e2-8165-734057cc59db&category_id=6320a497-50f1-4607-be84-efe14accbae6
Сколько существует 4-разрядных четверичных чисел, 
в которых хотя бы одна цифра встречается не менее двух раз?
0032 - не начинается с 0
174 - ответ
"""
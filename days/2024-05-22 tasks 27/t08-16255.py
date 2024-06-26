from itertools import product


cnt = 0
for combo in product('012345678', repeat=7):
    if combo[0] != '0':
        if combo[0] in '2468':
            if combo[-1] in '124578':
                if combo.count('6') >= 1:
                    cnt += 1

print(cnt)

"""
Определите количество семизначных чисел, записанных в девятеричной системе счисления, которые не начинаются с нечетных цифр, оканчиваются на цифры, не делящиеся на 3 без остатка, а также содержат в своей записи хотя бы одну цифру 6.
"""
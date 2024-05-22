# print(int('43333',5)+1)

# from itertools import product
# i = 0
# for combo in product('АПРСУ', repeat=5):
#     i += 1
#     if combo.count('У') <= 1 and  combo.count('А') == 0:
#         print(i)

from itertools import product
for i, combo in enumerate(product('АПРСУ', repeat=5), start=1):
    if combo.count('У') <= 1 and  combo.count('А') == 0:
        print(i)


"""
count 'У' <= 1 and  count 'А' == 0

01234
АПРСУ

"УСССС"
1 00000
X 43333(5) => X(10)

X+1

"""

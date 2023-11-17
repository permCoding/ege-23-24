from itertools import product


count = 0
combs = ["02", "20", "22", "42", "24"]
for item in product("012345", repeat=7):
    word = "".join(item)
    if word.count("2") == 1 and word[0] != '0':
        if all([not(combo in word) for combo in combs]):
        # if all([combo not in word for combo in combs]):
            count += 1

print(count)



# pos = word.index("2")
# слева и справа от pos


"""
Сколько существует шестеричных семизначных чисел, 
содержащих в своей записи ровно одну цифру 2, 
при этом никакая чётная цифра не стоит рядом с цифрой 2?
"""


# t = [1, 22, 3]
# # g = [x%2!=0 for x in t]
# g = list(map(lambda x: x%2!=0, t))
# print(g)
# print(all(g))

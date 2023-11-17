from itertools import product


count = 0
combs = "02,20,22,42,24".split(",")
for item in product("012345", repeat=7):
    word = "".join(item)
    if word.count("2") == 1 and word[0] != '0':
        pos = word.index("2")
        x = pos > 0 and word[pos-1] in "024"
        y = pos < len(word)-1 and word[pos+1] in "024"
        count += not(x or y)

print(count)

"""
Сколько существует шестеричных семизначных чисел, 
содержащих в своей записи ровно одну цифру 2, 
при этом никакая чётная цифра не стоит рядом с цифрой 2?
"""

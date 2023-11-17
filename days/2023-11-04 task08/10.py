from itertools import product


count = 0
combs = ["02", "20", "22", "42", "24"]
for item in product("012345", repeat=7):
    word = "".join(item)
    if word.count("2") == 1 and word[0] != '0':
        b = True
        for combo in combs:
            if combo in word:
            # if word.count(combo) > 0:
                b = False
                break
        if b:
            count += 1
       
print(count)

        # all !!!

# pos = word.index("2")
# слева и справа от pos


"""
Сколько существует шестеричных семизначных чисел, 
содержащих в своей записи ровно одну цифру 2, 
при этом никакая чётная цифра не стоит рядом с цифрой 2?
"""
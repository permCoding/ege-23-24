from itertools import product

for index, combo in enumerate(product("ИРЩЮ", repeat=5)):
    if combo[0] + combo[-1] == "ЩИ":
        print("".join(combo), index+1)

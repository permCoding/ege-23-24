from itertools import product

n = 0
for w in product("ИРЩЮ", repeat=5):
    n += 1
    if w[0] + w[-1] == "ЩИ":
        print("".join(w), n)

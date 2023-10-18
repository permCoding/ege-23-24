from itertools import product

count = 0
for combo in product("012345", repeat=7):
    s = "".join(combo)
    if s.count("2") == 1 and s[0] != "0":
        p = s.index("2")
        b = True
        if p > 0 and int(s[p-1])%2 == 0: b = False
        if p < len(s)-1 and int(s[p+1])%2 == 0: b = False
        if b: count += 1
        
print(count)

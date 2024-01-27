def f(x,y,w,z):
    return y and (x or z) or (not(y or z)) or w

for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if not(f(x,y,w,z)):
                    print(x,y,w,z)
"""
0 0 0 1
0 1 0 0
1 0 0 1
"""
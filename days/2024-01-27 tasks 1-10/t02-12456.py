def f(x,y,w,z):
    return not(y <= (x==w)) and (z <= x)

for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if f(x,y,w,z):
                    # print(z,x,y,w)
                    print(w,x,y,z)
"""
1 0 1 0
0 1 1 0
0 1 1 1
"""
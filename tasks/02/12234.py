def f(x, y, z, w):
    return y and (x or z) or not(y or z) or w

val = [False, True]
for x in val:
    for y in val:
        for z in val:
            for w in val:
                if not(f(x,y,z,w)):
                    print(+x,+y,+w,+z)

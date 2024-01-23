def f(x,y,w,z):
    return y and (x or z) or not(y or z) or w

for x in False, True:
    for y in False, True:
        for w in False, True:
            for z in False, True:
                if not(f(x,y,z,w)):  # xyzw
                    print(+x,+y,+z,+w)

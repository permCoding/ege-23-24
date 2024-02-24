def f(x,y,z,w):
    return (x and y) or (y == z) or (w)

for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not(f(x,y,z,w)):
                    print(z,y,x,w)

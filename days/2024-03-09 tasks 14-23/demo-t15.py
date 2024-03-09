def f(x, y, A):
    return (x+2*y<A) or (y>x) or (x>60)


diap = list(range(300))
for A in diap:
    b = True
    for x in diap:
        for y in diap:
            if f(x, y, A) == False:
                b = False
    if b:
        print(A)

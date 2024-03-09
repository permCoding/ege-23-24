def f(x, y, A):
    return (x+2*y<A) or (y>x) or (x>60)


d = list(range(300))
for A in d:
    if all(f(x, y, A) for x in d for y in d):
        print(A)
        break

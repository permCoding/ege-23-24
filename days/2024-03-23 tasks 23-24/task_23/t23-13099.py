def f(a, cmd):
    if a in [15, 16]: return 1
    if a > 15: return 0
    sm = f(a*2, 2) + f(a*3, 3)
    if cmd != 1: sm += f(a-1, 1)
    return sm


print(f(3, 0))

# дорешать второе условие
# при этом не содержат двух команд A подряд?

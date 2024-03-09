def f(a):
    if a > 16: return 0
    if a == 15: return 1
    return f(a-1) + f(a*2) + f(a*3)


print(f(3))

# дорешать второе условие
# при этом не содержат двух команд A подряд?

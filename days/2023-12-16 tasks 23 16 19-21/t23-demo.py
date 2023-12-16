def get(a, b):
    if a == b: return 1
    # if a > b: return 0
    if a > b: return 0
    if a == 11: return 0
    return get(a+1,b) + get(a*2,b) + get(a**2,b)


print(get(2, 20))  # -11
# print(get(2, 11) * get(11,20))  # +11

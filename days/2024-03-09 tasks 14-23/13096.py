def to_int_1(t):
    base = 39
    p = 0
    res = 0
    for elm in t[::-1]:
        res += elm * base ** p
        p += 1
    return res  # из 39-ричной


def to_int_2(t):
    base = 39
    p = len(t) - 1
    res = 0
    for elm in t:
        res += elm * base ** p
        p -= 1
    return res  # из 39-ричной


for x in range(39):  # 0 .. 38
    for y in range(39):  # 0 .. 38
        t = (5,8,x,7,2,3,y,4,9)
        # d = to_int_1(t)
        d = to_int_2(t)
        if d % 38 == 0:
            num = y*39**1 + x*39**0
            if int(num**.5) ** 2 == num:
                print(x, y , num)

"""
3210
002A(16) = 2*16**1 + A*16**0 = 42(10)
"""

# 21 => 2*16**1 + 1*16**0 => 33(10)
# num = 16
# print((num**.5))
# print((num**.5)**2)
# print((num**.5)**2 == num)



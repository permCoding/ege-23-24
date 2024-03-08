def to_int(t):
    return 12653416  # из 39-ричной

for x in range(39):
    for y in range(39):
        t = (5,8,x,7,2,3,y,4,9)
        d = to_int(t)
        if d % 38 == 0:
            num = y*39+x
            if (num**.5)**2 == num:
                print(num)



# 21 => 2*16**1 + 1*16**0 => 33(10)
# num = 10
# print((num**.5)**2 == num)

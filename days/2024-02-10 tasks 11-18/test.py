ip = 6   # 00000110 bit
ms = 12  # 00001100

res = bin(ip & ms)[2:]
print(res.zfill(8))
print(f'{res:>08}')

# 00000110
# 00001100
# --------
# 00000100 &   4
# 00001110 |  14
# 00001010 ^  10

print(ip & ms)
print(ip | ms)
print(ip ^ ms)

ip = '136.36.240.16'
ms = '255.255.255.248'

for last in range(16, 23+1):
    b = [
        bin(136)[2:].zfill(8),
        bin(36)[2:].zfill(8),
        bin(240)[2:].zfill(8),
        bin(last)[2:].zfill(8),
    ]
    print(''.join(b))

# ms = 11111111.11111111.11111111.11111000

# ip_a = 100010000010010011110000 00010000
# ...
# ip_b = 100010000010010011110111 00010111

# print(bin(248)[2:])  # 11111000

# 000
# ...
# 111
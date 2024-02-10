ip = '192.168.32.160'
ms = '255.255.255.240'
print(bin(240), bin(160))
ms = '11111111.11111111.11111111.11110000'

t = [int(x) for x in ip.split('.')]
k = 0
for last in range(160, 176):
    t[-1] = last
    s = [bin(e)[2:].zfill(8) for e in t]  # [192, 168, 32, '160']
    s = ''.join(s)
    if s.count('1') % 2 == 0:
        k += 1
print(k)

# print(int('10101111',2))

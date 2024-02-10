ip = '10110011'
address = int(ip, 2)
print(address)  # 179

# ip = '10110011'
# ms = '00011111'
ms_home = 31
print(address & ms_home)  # =================
print(bin(address & ms_home)[2:])

print(address >> 5) # 10110011 -> 00000101
ms_street = int('11100000', 2)
print(ms_street)

print((address & ms_street) >> 5)  # =================
print(address & ms_home)  # =================



"""
00000000
10110011 

5 - улица
19 - номер

8 - улиц
32 - номер дома
"""
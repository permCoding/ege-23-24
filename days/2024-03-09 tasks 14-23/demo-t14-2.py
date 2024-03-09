dec = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024

base = 25
while dec > 0:
    print(dec % base)
    dec //= base
# 9

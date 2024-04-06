s = open("./24_12946.txt").readline()
# s = "AD4T5T6T7Y66Y66"

al = "QWERTYUIOPASDFGHJKLZXCVBNM"
# al = ''.join(chr(i) for i in range(65, 91))
nu = "0123456789"

max_size = size = 0
for i in range(len(s)-1):
    u1 = s[i] in al and s[i+1] in al
    u2 = s[i] in nu and s[i+1] in nu
    if u1 or u2:
        size = 1
    else:
        size += 1
        max_size = max(max_size, size)
print(max_size)

# A = 65
# print(ord('A'), ord('Z'))
# print(chr(65))
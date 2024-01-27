k, n = 0, 0
while True:
    n += 1
    s = str(n)
    if len(s)==5 and s[0] != '0' and s.count('9') == 0 and s.count('5') == 1:
        if s[0]!=s[1] and s[1]!=s[2] and s[2]!=s[3] and s[3]!=s[4]:
            k += 1
    if len(s)>5: break
print(k)  # 13377
"""
девятеричных пятизначных чисел, 
ровно одну цифру 5, 
никакие две одинаковые цифры не стоят рядом
"""
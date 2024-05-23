s = open('./16333.txt').readline()

mx, ln = 1, 1
prev = s[0] in 'QRW'
for i in range(1, len(s)):
    cur = s[i] in 'QRW'
    if prev != cur:
        ln += 1
        mx = max(mx, ln)
    else:
        ln = 1
    prev = cur
print(mx)

"""
Текстовый файл состоит из Q, R, W и цифр 1, 2, 4
Определите максимальное количество идущих подряд символов, 
среди которых ни одна буква не стоит рядом с буквой, а цифра – с цифрой. 

Q1R1R1W2 +
Q1R1QR1W24 --
"""
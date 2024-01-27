from itertools import product

def check(elm):
    for i in range(len(elm)-1):
        if elm[i]==elm[i+1]: return False
    return True

k, al = 0, '012345678'
for elm in product(al, repeat=5):
    if elm[0] != '0' and elm.count('5') == 1:
        # if elm[0]!=elm[1] and elm[1]!=elm[2] and elm[2]!=elm[3] and elm[3]!=elm[4]:
        if check(elm):
            k += 1
print(k)  # 13377
"""
девятеричных пятизначных чисел, 
ровно одну цифру 5, 
никакие две одинаковые цифры не стоят рядом
"""
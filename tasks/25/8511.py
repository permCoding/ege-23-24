for n in range(0, 10**8+1, 253):
    s = str(n)
    if s[:2] == '12' and s[4:6] == '15' and s[-1] == '6':
        print(s, n//253)

'''
Среди натуральных чисел, 
не превышающих 10**8, найдите все числа, 
соответствующие маске 12??15*6, 
делящиеся на 253 без остатка.
1278156 5052
12531596 49532
12741586 50362
12951576 51192
'''
def is_prime(num):
    for d in range(2, int(num**.5) + 1):
        if num % d == 0: return False
    return True


for num in range(1, 10**7+1):
    s = str(num)
    if s[0]=='3' and s[2:6]=='1111':
        if is_prime(num):
            print(num)

"""

3?1111*

1 * 9 == 9
2 * 4.5 == 9
3 * 3 == 9
4 * 2.25 == 9
"""
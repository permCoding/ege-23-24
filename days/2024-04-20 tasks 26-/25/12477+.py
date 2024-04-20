def get_primes(n):
    primes = [i for i in range(0, n+1)]
    primes[1] = 0
    for i in range(2, n+1):
        if primes[i] != 0:
            for j in range(i+i, n+1, i):
                primes[j] = 0
    return [elm for elm in primes if elm != 0]


n = 10**7+1
primes = get_primes(n)
for num in range(1, n):
    s = str(num)
    if s[0]=='3' and s[2:6]=='1111' and num in primes:
        print(num)

"""

3?1111*

1 * 9 == 9
2 * 4.5 == 9
3 * 3 == 9
4 * 2.25 == 9
"""
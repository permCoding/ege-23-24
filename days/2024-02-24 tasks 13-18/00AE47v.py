def to_base(n, base):
    res = ''
    while n > 0:
        res = str(n%base) + res
        n //= base
    return res


# al = '0123456' # 'АЖИМНУЧ'
cnt = 0
for n in range(0, int('666666',7)+1):  # 117648
    word = to_base(n, 7).zfill(6)
    if (n+1)%2 == 0:
        if word[0] != '1' and word.count('6') <= 1:
            cnt += 1
print(cnt)  # 39528
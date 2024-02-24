from itertools import product


al = 'АЖИМНУЧ'

cnt = 0
for n,elm in enumerate(product(al, repeat=6), start=1):
    if n%2 == 0:
        if elm[0] != 'Ж' and elm.count('Ч') <= 1:
            cnt += 1
    # print(''.join(elm), n)

print(cnt)  # 39528

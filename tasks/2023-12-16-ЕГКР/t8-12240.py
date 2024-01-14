from itertools import product

iter = product(list('012345678'), repeat=5)
cnt = 0
for y in iter:
    if y.count('5') == 1 and y[0] != '0':
        if y[0] != y[1] and y[1] != y[2] and y[2] != y[3] and y[3] != y[4]:
            cnt += 1
print(cnt)  # 13377
def f(n):
    b = bin(n)[2:]
    if n%2==0:
        b += b[-2:]
    else:
        b = '1' + b + '0'
    return int(b, 2)

for n in range(1000, 1, -1):
    if f(n) < 100:
        print(n)  # 24
        break

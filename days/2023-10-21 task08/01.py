def to_bin(n):
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b


num = 13
print(to_bin(num))
print(bin(num)[2:])

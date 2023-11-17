from math import pi

print(pi)

n = 12
print(n + (n & 1))  # 0b1100 & 0b0001 == 0b0000 => 0
n = 13
print(n + (n & 1))  # 0b1101 & 0b0001 == ob0001 => 1

# version

n = 12
print(n + [10, -11][n & 1])

n = 13
print(n + [10, -11][n & 1])

f = open('./8513-B.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mx, mx_a = 0, 0
for i in range(n-k):
    a, b = t[i], t[i+k]
    mx_a = max(mx_a, a)
    mx = max(mx, mx_a+b)

print(mx)  # B=2090920

"""
# for i in range(k, n):
#     a, b = t[i-k], t[i]

for i in range(n-k):
    b = t[i+k]
    max_a = max(t[:i+1])
    mx = max(mx, max_a+b)

Определите два таких переданных числа, чтобы между моментами их передачи прошло не менее K мин., а их сумма была максимально возможной. Укажите найденное суммарное количество осадков.
"""
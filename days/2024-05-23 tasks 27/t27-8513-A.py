f = open('./8513-A.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mx = 0
# for i in range(n):
#     for j in range(n):
#         if j-i>=k:
#             sm = t[i]+t[j]
#             if sm > mx:
#                 mx = sm

for i in range(0, n-k):
    for j in range(i+1, n):
        mx = max(mx, t[i]+t[j])

print(mx)  # A=1219

"""
Определите два таких переданных числа, чтобы между моментами их передачи прошло не менее K мин., а их сумма была максимально возможной. Укажите найденное суммарное количество осадков.
"""
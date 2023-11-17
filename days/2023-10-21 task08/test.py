# n = int(input())
# t = sorted(list(bin(n)[2:]), reverse=True)
# r = int("".join(t), 2)
# print(r)
#
# t = []
# for n in range(1, 1000):
#     b = bin(n)[2:]
#     if n%3 == 0: b += b[-3:]
#     else: b += bin((n%3)*3)[2:]
#     r = int(b, 2)
#     if r < 170: t.append(r)
# print(sorted(t, reverse=True))
#
# from itertools import product
# alph = "ИРЩЮ"
# k = 0
# for combo in product(alph, repeat=5):
#     k += 1
#     if combo[0] == "Щ" and combo[-1] == "И":
#         print(k)
#
# ИРЩЮ
# 0123
# 2...0
# 23330
# 3*4**1 + 3*4**2 + 3*4**3 + 2*4**4 = 764 + 1
# def get(x):
#     r = ''
#     while x > 0:
#         r = str(x%4) + r
#         x //= 4
#     return r
#
# n = 0
# while True:
#     r = get(n)
#     n += 1
#     if len(r) < 5: continue
#     if len(r) > 5: break
#     if r[0] == "2" and r[-1] == "0":
#         print(n)
#
# k = 0
# a = set(list("0123"))
# for n in range(100000):
#     s = str(n)
#     b = set(list(s))
#     if b <= a:
#         k += 1
#         if len(s) == 5 and s[0] == "2" and s[-1] == "0":
#             print(n, k)

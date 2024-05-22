def to27(n, base=27):
    s = []
    while n > 0:
        s = [n%base] + s
        n //= base
    return s

n = 2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024

x = to27(n) # print(x)

alph = map(int, '0123456789')  # print(list(alph))
cnt = sum([x.count(elm) for elm in alph])
print(len(x)  -cnt)  # 2687

# cnt = 0
# for ch in x:
#     if ch not in alph:
#         cnt += 1
# print(cnt)
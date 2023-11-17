# https://inf-ege.sdamgia.ru/test?theme=221

# Укажите наименьшее число, в результате обработки
# которого автомат выдаст число 1412.

for num in range(100, 1000):
    s = str(num)  # 012
    a, b = int(s[0])+int(s[1]), int(s[1])+int(s[2])
    mx, mn = max(a, b), min(a, b)
    if str(mx) + str(mn) == "1412":
        print(num)
        break

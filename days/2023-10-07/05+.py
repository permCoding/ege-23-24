# https://inf-ege.sdamgia.ru/test?theme=221

# Укажите наименьшее число, в результате обработки
# которого автомат выдаст число 1412.
def get(num):
    t = list(map(int, str(num)))
    t = sum(t[:2]), sum(t[1:])
    return str(max(t)) + str(min(t)) == "1412"


print(min([num for num in range(100, 1000) if get(num)]))

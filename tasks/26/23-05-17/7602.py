f = open('./7602.txt')
k = int(f.readline())  # количество ячеек в камере хранения
n = int(f.readline())  # количество пассажиров, сдающих багаж
t = [list(map(int, f.readline().split())) for _ in range(n)]
t.sort(key=lambda e: (e[0],e[1])) # [время сдачи багажа, время выдачи багажа]

cells = [0]*k  # ячейки хранилища - время их освобождения
count = 0  # сданных багажей

# берём i-й багаж и пытаемся пристроить в ячейку
for i in range(n):  # по всем багажам
    for j in range(k):  # по всем ячейкам
        if t[i][0] > cells[j]:  # вр сдачи больше чем вр освобожд
            cells[j] = t[i][1]  # запишем в ячейку вр забирания багажа
            count += 1  # сдали ещё 1 багаж
            break  # этот багаж уже сдали - идём к следующему
print(count, j+1)  # 586 3

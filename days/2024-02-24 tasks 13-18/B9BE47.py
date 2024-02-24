cnt = 0
for line in open('./B9BE47.csv'):
    # t = sorted(int(elm) for elm in line.split(';'))
    t = sorted(map(int, line.split(';')))
    if (t[0] + t[4])**2 > t[1]**2 + t[2]**2 + t[3]**2:
        cnt += 1
print(cnt)  # 2623

"""
квадрат суммы максимального и минимального 
чисел в строке больше 
суммы квадратов трёх оставшихся
"""
t = [int(e) for e in open("17_6024.txt").readlines()]
m = max(e for e in t if e%100==12)
##m = max(filter(lambda x: x%100==12, t))

k, sm = 0, 0
for i in range(len(t)-1):
    a,b = t[i],t[i+1]
    if (a+b)**2 < m**2:
        if (a%100==12) ^ (b%100==12):
            k+=1
            sm = max(sm, a+b)
print(k, sm)
"""
35

Определите количество пар последовательности,
в которых только один из элементов
оканчивается на 12, а квадрат суммы элементов
пары меньше квадрата максимального элемента
последовательности, оканчивающегося на 12.
В ответе запишите количество найденных пар,
затем максимальную из сумм элементов таких пар. 

"""

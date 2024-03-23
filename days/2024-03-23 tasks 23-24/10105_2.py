s = open('./10105.txt').readline()

countT = 100

t = [i for i in range(len(s)) if s[i]=='T']
sizes = []
for pos_l in range(len(t) - countT - 1):
    pos_r = pos_l + countT + 1
    size = t[pos_r]-t[pos_l]-1
    sizes.append(size)
print(max(sizes))




"""
Определите в прилагаемом файле 
максимальное количество идущих подряд символов, 
среди которых символ T встречается ровно 100 раз.
"""
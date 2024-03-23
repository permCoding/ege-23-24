s = open('./10105.txt').readline()

k = 100

t = [i for i in range(len(s)) if s[i]=='T']

print(max(t[pos_l+k+1]-t[pos_l]-1 for pos_l in range(len(t)-k-1)))


"""
Определите в прилагаемом файле 
максимальное количество идущих подряд символов, 
среди которых символ T встречается ровно 100 раз.
"""
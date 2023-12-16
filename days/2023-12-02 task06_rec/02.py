from random import randint as r

size = 9
f = open("./csv/table.csv", 'w')
for y in range(1, size+1):
    row = [str(r(1,19)) for x in range(1,size+1)]
    f.write(" ".join(row) + '\n')
f.close()
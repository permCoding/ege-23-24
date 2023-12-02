from random import randint as r

size = 6
f = open("./table.csv", 'w')
for y in range(1, size+1):
    row = [str(r(10,99)) for x in range(1,size+1)]
    f.write(" ".join(row) + '\n')
f.close()
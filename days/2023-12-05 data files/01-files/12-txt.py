f = open('./data/lang_rate.txt')
lines = f.readlines()
f.close()

for line in lines:
    lst = line.strip().split(";")
    print(lst[1])

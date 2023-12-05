f = open('./data/lang_rate.txt')
lines = f.readlines()
f.close()

for line in lines:
    print(line.strip())
    # print(line, end="")

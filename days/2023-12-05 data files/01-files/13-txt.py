f = open('./data/lang_rate.txt')
lines = f.readlines()
f.close()

langs = []
for line in lines:
    lst = line.strip().split(";")
    langs.append(lst[1])
    # langs += [lst[1]]

langs.sort()

print(langs)

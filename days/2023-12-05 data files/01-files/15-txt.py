f = open('./data/lang_rate.txt')
lines = f.readlines()
f.close()

langs = []
for line in lines:
    lst = line.strip().split(";")
    langs.append(lst[1])

langs_sorted = sorted(langs, key=lambda elm: len(elm))

for lang in langs_sorted:
    print(lang)

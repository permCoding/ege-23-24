def get_key(elm):
    return len(elm)


f = open('./data/lang_rate.txt')
lines = f.readlines()
f.close()

langs = []
for line in lines:
    lst = line.strip().split(";")
    langs.append(lst[1])

langs_sorted = sorted(langs, key=get_key)

for lang in langs_sorted:
    print(lang)

from module import get


url = 'https://pcoding.ru/parsing/03/page.html'
txt = get(url)

# print(type(txt))
taga, tagb = '<title>', '</title>'
posa = txt.find(taga) + len(taga)
posb = txt.find(tagb)
print(txt[posa:posb])


from bs4 import BeautifulSoup as BS


f = open('./data/page.html', 'r', encoding='utf8')
html = f.read()
f.close()

sp = BS(html, 'html.parser')

trs = sp \
    .find('table', id='students') \
    .find_all('tr', class_='tr__data')

students = []
for tr in trs:
    tds = tr.find_all('td')
    student = {
        'name': tds[0].text.strip(),
        'group': tds[1].text.strip(),
        'ball': int(tds[2].text.strip())
    }
    students.append(student)
    
print(students)

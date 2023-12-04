import csv

f = open('./data/exam_balls.csv')

reader = csv.reader(f, delimiter=";")
headers = next(reader)  # читаем строку заголовков
print(*headers)

for item in reader:
    if item[2] == "м":
        print(*item)

f.close()

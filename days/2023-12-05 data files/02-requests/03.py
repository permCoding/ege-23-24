import requests
import csv


filename = "https://pcoding.ru/csv/abiturs.csv"

response = requests.get(filename)
response.encoding = "utf8"
lines = response.text.split("\n")

reader = csv.reader(lines, delimiter=",")

headers = next(reader)  # читаем строку заголовков

abiturs = list(reader)  # данные
rows = list(map(lambda x: x[:3], abiturs))

# rows.sort(key=lambda x: -int(x[2]))

with open("./rate.csv", "w", encoding="utf8") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(headers[:3])  # записать строку заголовков
    writer.writerows(rows)  # записать все строки с данными

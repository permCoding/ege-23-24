import csv


def get_data(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=";")
        headers = next(reader)  # читаем строку заголовков
        rows = [row for row in reader]
    return (headers, rows)


def process_data(rows, direct, limit):
    res = [row for row in rows if int(row[-1]) == direct]
    res.sort(key=lambda x: int(x[3])+int(x[4])+int(x[5]), reverse=True)
    return res


def to_file(data, headers):
    print(headers)
    for row in data:
        print(row)


headers, rows = get_data('./data/exam_balls.csv')
data = process_data(rows, 1, 5)
to_file(data, headers)

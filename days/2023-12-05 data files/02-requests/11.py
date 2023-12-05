import requests


def get_lines(url):
    response = requests.get(url)
    response.encoding = "utf8"
    return response.text.splitlines()


def get_data(lines):
    pairs = [line.strip().split(';') for line in lines]
    return map(lambda pair: [float(pair[0].replace(",",".").strip("%")), pair[1]], pairs)


url = "https://pcoding.ru/txt/labrab04-3.txt"
lines = get_lines(url)
data = get_data(lines)

for elm in sorted(data, key=lambda pair: pair[0], reverse=True):
    print(f"{elm[0]:<8.2f}{elm[1]}")

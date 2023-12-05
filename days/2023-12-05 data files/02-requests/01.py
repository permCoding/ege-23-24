import requests
import csv


filename = "https://pcoding.ru/txt/labrab04-3.txt"

response = requests.get(filename)
response.encoding = "utf8"
lines = response.text.split("\n")

for line in lines: print(line)

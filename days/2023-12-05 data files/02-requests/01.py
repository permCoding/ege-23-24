import requests  # pip install requests


url = "https://pcoding.ru/txt/labrab04-3.txt"

response = requests.get(url)
response.encoding = "utf8"
lines = response.text.splitlines()  # \n \r\n

for line in lines: print(line)

# Uniform Resource Locator - url

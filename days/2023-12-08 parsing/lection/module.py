import requests  # pip install requests


def get(url):
    response = requests.get(url)
    response.encoding = "utf8"
    return response.text

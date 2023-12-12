from wget import download
from requests import get


def load_file_1(url, folder, filename):
    with open(f"{folder}{filename}", 'wb') as f:
        f.write(get(url).content)


def load_file_2(url, folder, filename):
    download(url, f"{folder}{filename}")


# url = 'https://kompege.ru/img/logo.2815aead.png'
# url = 'https://pcoding.ru/pdf/PythonJunior.pdf'
# url = 'https://pcoding.ru/fon/bbb51.png'
# url = 'https://kompege.ru/img/logo.2815aead.png'
# url = 'https://rur.hitmotop.com/get/music/20190330/Billie_Eilish_-_bad_guy_63154737.mp3'
url = 'https://kompege.ru/files/-sp1xqL_c.xlsx'
folder = './files/'
filename = url.split('/')[-1]
load_file_1(url, folder, filename)
# load_file_2(url, folder, filename)

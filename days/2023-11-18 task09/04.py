import requests

url = "https://pcoding.ru/csv/09_2100.txt"
resp = requests.get(url)  # open()
lines = resp.text.split('\n')

lst = []
for line in lines:
    nums = sorted([int(e) for e in line.split(";")])
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        lst.append(nums[0] + nums[1])
print(max(lst))

"""
https://pcoding.ru/csv/09_2100.txt
http://parsing.1gb.ru/temp/Perm
https://pcoding.ru/fon/proCoding.png
https://pcoding.ru/pdf/sort.pdf
"""
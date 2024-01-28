import re


for line in open('./date.txt').readlines():
    print(re.sub(r'\s*[-./]\s*', '.', line), end='')

"""

['12-01-2024\n', '12.02.2023\n', '23/03/2022\n', '12 -01 -2024\n', '12 - 01 - 2024\n', '12      -01 -     2024']

"""
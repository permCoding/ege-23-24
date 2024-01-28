import re


lst = [
    '23.01.2024',
    '23/01/2024',
    '23-01-2024',
    '23-01.2024',
]

# ptn = r'\.|\/|\-'
ptn = r'[-./]'
for elm in lst:
    # print(elm.split('.'))
    res = re.split(ptn, elm)
    print(res)

# line = '123\n456\r789\r666\n999\n10'
# with open('./test.txt', 'w') as f:
#     f.write(line)

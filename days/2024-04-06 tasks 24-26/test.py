t = ['000120', 'A0D', 'FFF0004', 'E']

# res = max(t, key=len)

def getAmountZero(line):
    return line.count('0')

# res = max(t, key=getAmountZero)

res = max(t, key=lambda line: line.count('0'))

print(len(res))

t.sort(key=getAmountZero, reverse=True)
print(t)
# sort
# sorted

import re

print(re.search('[^0]', '').span())

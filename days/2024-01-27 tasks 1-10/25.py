import re
import fnmatch

p = re.compile('^12.3.*456..9$')

for n in range(98591, 10**12+1, 98591):
    s = str(n)
    # if s[:2]=='12' and s[3]=='3' and s[-6:-3]=='456' and s[-1]=='9':  # 4 sec
    if p.match(s):  # 7.1
    # if re.match('^12.3.*456..9$', s):  # 11.2 sec
    # if re.match('^12\d3\d*456\d{2}9$', s):  # 11.6 sec
    # if fnmatch.fnmatch(s, '12?3*456??9'):  # 25.6 sec
        print(n, n//98591)

# 12?3*456??9

"""
120313456439 1220329
120383456049 1221039
125351456539 1271429
"""
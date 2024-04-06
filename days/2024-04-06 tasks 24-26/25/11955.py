import re
from fnmatch import fnmatch


def f1(s):
    uBase = s[0]=='1' and s[2:6]=='2157' and s[-1]=='4'
    uA = s[1] in '02468'
    uB = set(s[6:-1]) <= set('13579')
    return uA and uB and uBase


def f2(s):
    return fnmatch(s, '1?2157*4')


def f3_re(s):
    return re.match('^1[02468]2157[13579]*4$', s)


def f3_re_speed(s):
    return ptn.match(s)


ptn = re.compile('^1[02468]2157[13579]*4$')
for num in range(133, 10**10+1, 133):
    if f3_re_speed(str(num)):
        print(num, num//133)


# s = '1A2157B4'
# s = '17237726'
# print(set(s[3:-1]) <= set('13579'))
# print(set('') <= set('13579'))

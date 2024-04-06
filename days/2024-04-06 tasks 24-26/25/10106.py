from re import match
from fnmatch import fnmatch

def f1(s): return s[0]=='1' and s[2:6]=='2157' and s[-1]=='4'
def f2(s): return fnmatch(s, '1?2157*4')
def f3(s): return match('1.2157.*4', s)

for num in range(2024, 10**10+1, 2024):
    if f3(str(num)):
        print(num, num//2024)
    
'''
142157664 70236
1021575544 504731
1121571264 554136
1221577104 603546
1321572824 652951
1421578664 702361
1521574384 751766
1621570104 801171
1721575944 850581
1821571664 899986
1921577504 949396
'''

# print(fnmatch('1221577104', '1?2157*4'))
# print(match('1.2157.*4', '1221577104'))
# print(match('1.2157.*4', '19921577104'))

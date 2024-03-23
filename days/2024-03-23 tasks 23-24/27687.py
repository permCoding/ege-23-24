def f1(s):
    cr, mx = 1, 1
    for i in range(len(s)-1):
        if s[i:i+2] == 'YY':
            cr += 1
            if cr > mx: mx = cr 
        else:
            cr = 1
    print(mx)

def f2(s):
    for i in range(1, 10**4):
        if s.find('Y'*i) < 0:
            print(i-1)
            break


def f3(s):
    s = s.replace('X','.').replace('Z','.')
    t = s.split('.')
    print(max(len(elm) for elm in t))


def f4(s):
    s = s.replace('X','.').replace('Z','.')
    t = s.split('.')
    print(len(max(t, key=len)))


s = open('./27687.txt').readline()
f4(s)


"""
Определите длину самой длинной 
последовательности, состоящей из символов Y.

XXXYYYYXYZXZXYYYYYYYYXZ
...YYYY.Y....YYYYYYYY..
"""
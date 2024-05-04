def f1():
    dct = dict()
    for key in t:
        if dct.get(key):
            dct[key] += 1
        else:
            dct[key] = 1
    val = max(dct.values())
    elm = max(dct, key=dct.get)
    print(val, elm)


def f2():
    values = [0] * (max(t)+1)
    for key in t: values[key] += 1
    max_val = max(values)
    ind = values.index(max_val)
    print(ind, max_val)


def f3():  # сортировка подсчётом
    cntrs = [0] * (max(t)+1)
    for elm in t: cntrs[elm] += 1
    srtd = []
    for i in range(len(cntrs)):
        tmp = [i] * cntrs[i]  # [2,2,2,2]
        srtd += tmp  # srtd.extend( tmp )
    print(srtd)

    
t = [1,3,2,2,0,3,2,2,1, 99, 7]


# f1()
# f2()
f3()

"""
key, val = 2, 555
dct[key] = val
print(2 in dct.keys())
print(dct.get(key))
# if key in dct.keys():
#     dct[99] = 1
#     # dct[99] += 1
"""
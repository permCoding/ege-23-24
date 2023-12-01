def get(p, combo):
    if len(p) == 0:
        print(combo)
    else:
        get(p[1:], combo+[p[0]])
        get(p[1:], combo)    

t = ['a', 'b', 'c']
get(t, [])

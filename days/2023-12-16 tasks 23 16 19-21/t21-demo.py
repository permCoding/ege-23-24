def ch(st, t):
    if st in [1,3]: return all(t)
    return any(t)

def g(s, st):
    if s>=129: return st in [2,4]
    if st == 4: return False
    st += 1
    t = [g(s+1, st), g(s*2, st)]
    return ch(st, t)

for s in range(1, 129):
    if g(s, 0): print(s)

""" 62
  0  19  20  21
П 1
В 2  __
П 3      __
В 4          __
"""
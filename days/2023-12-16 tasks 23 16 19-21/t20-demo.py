def ch(st, t):
    if st == 2: return all(t)
    return any(t)

def g(s, st):
    if s>=129: return st == 3
    if st == 3: return False
    st += 1
    t = [g(s+1, st), g(s*2, st)]
    return ch(st, t)

for s in range(1, 129):
    if g(s, 0): print(s)

""" 32 63
  0  19  20  21
П 1
В 2  __
П 3      __
В 4          __
"""
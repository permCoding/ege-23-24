def get(s, st):
    if st == 1 and s >= 129: return False
    if st == 0 and s >= 129: return True
    if st == 0 and s < 129: return False
    st -= 1
    a = get(s+1, st)
    b = get(s*2, st)
    if st == 1: return a and b
    if st == 0: return a or b

def get_(s, st):
    if st == 1 and s >= 129: return False
    if st == 0 and s >= 129: return True
    if st == 0 and s < 129: return False
    st -= 1
    a, b = get(s+1, st), get(s*2, st)
    if st == 1: 
        return a and b
    else:
        return a or b

for s in range(1, 129):
    # if get(s, 2): print(s)  # 64
    if get_(s, 2): print(s)
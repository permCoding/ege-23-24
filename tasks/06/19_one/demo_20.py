def get(s, st):
    if st == 0: return s >= 129
    if st == 1 and s >= 129: return False
    st -= 1
    a, b = get(s+1, st), get(s*2, st)
    return (a and b) if st == 1 else (a or b)

for s in range(1, 129):
    if not(get(s,1)) and get(s,3): print(s)  # 32 63
def get(s, st):
    if s >= 129: return st%2==0
    if st == 0: return False
    st -= 1
    a, b = get(s+1, st), get(s*2, st)
    return (a and b) if st%2==1 else (a or b)

for s in range(1, 129):
    if get(s,4) and not(get(s,2)): print(s)  # 62

# and - это при любой игре
#  or - это есть выигрышная
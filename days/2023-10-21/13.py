def get(n):
    res = ""
    while n > 0:
        res = str(n % 4) + res
        n //= 4
    return res


n = 0
while True:
    n += 1
    w = get(n)
    if len(w) < 5: continue
    if w[0] + w[-1] == "20": print(w, n)
    if len(w) > 5: break

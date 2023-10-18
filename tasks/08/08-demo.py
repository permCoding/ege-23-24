count = 0
n = 4095
while True:
    n += 1
    o = oct(n)[2:]
    if len(o) == 6: break
    if o.count('1') == 0 and len(set(list(o))) == len(o):
        p = [1 for i in range(4) if int(o[i])%2 != int(o[i+1])%2]
        if sum(p) == 4:
        # a = int(o[0])%2 != int(o[1])%2
        # b = int(o[1])%2 != int(o[2])%2
        # c = int(o[2])%2 != int(o[3])%2
        # d = int(o[3])%2 != int(o[4])%2
        # if a and b and c and d:
            count += 1
print(count)

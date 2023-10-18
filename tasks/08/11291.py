count = 0
for n in range(1000000, 5555555+1):
    s = str(n)
    if s.count("6") == 0 and s.count("7") == 0 and s.count("8") == 0 and s.count("9") == 0:
        if s.count("2") == 1:
            p = s.index("2")
            b = True
            if p > 0 and s[p-1] in "02468": b = False
            if p < len(s)-1 and s[p+1] in "02468": b = False
            if b: count += 1
            
print(count)

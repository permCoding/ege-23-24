s = open('./24_10105.txt').readline()

max_len, cnt_T, a = 0, 0, 0

for b in range(len(s)):

    if s[b] == 'T':
        cnt_T += 1
        while cnt_T > 100:
            a += 1
            if s[a-1] == 'T':
                cnt_T -= 1
    
    if cnt_T == 100:
        max_len = max(max_len, b-a+1)

print(max_len)

lines = open('./16328.txt').readlines()
t = [int(line) for line in lines]

mn = min(filter(lambda x: x%19==0, t))
cnt, mx = 0, 0
for i in range(0, len(t)-1):
    a, b = t[i]%mn==0, t[i+1]%mn==0
    if a or b:
        cnt += 1
        mx = max(mx, t[i]+t[i+1])
print(cnt, mx)
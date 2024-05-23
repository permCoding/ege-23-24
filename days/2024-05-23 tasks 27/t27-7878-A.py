f = open('./7878-A.txt')
n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mn = 2**30
for i in range(n):
    for j in range(n):
        if j-i>=k:
            p = t[i]*t[j]
            if p%157==0:
                mn = min(mn, p)
print(mn)  # T=6437 A=2958822 B=75360

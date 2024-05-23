f = open('./7878-B.txt')
n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mn, mn_a, mn_157 = 2**30, 2**30, 2**30
for i in range(n-k):
    a, b = t[i], t[i+k]
    if a%157==0: mn_157 = min(mn_157, a)
    mn_a = min(mn_a, a)
    a = mn_a if b%157==0 else mn_157
    mn = min(mn, b*a)
    
print(mn)  # T=6437 A=2958822 B=75360

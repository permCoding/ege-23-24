# f = open('./27-A_12934.txt')
f = open('./27-B_12934.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for i in range(n)]


mx_ln, sm = 0, 0
lt, rt = 0, 0
while rt < n:
    sm += t[rt]
    while sm > k:
        sm -= t[lt]
        lt += 1
    mx_ln = max(mx_ln, rt-lt+1)
    rt += 1
print(mx_ln)

# lt ... ... ... rt => <=k  >k
# ... lt ... ... rt => <=k

"""
Определите непрерывный отрезок времени максимальной длины, 
в течение которого сумма осадков была не более K.
0 1 2 3 4
2 - 0 = 2 + 1
"""
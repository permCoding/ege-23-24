# f = open('./27-A_12934.txt')
f = open('./27-B_12934.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for i in range(n)]

def A1():
    mx_ln = 0
    for lt in range(0, n):
        for rt in range(lt, n):
            sm = sum(t[lt:rt+1])
            if sm <= k:
                mx_ln = max(mx_ln, rt-lt+1)
    print(mx_ln)  # 108

def A2():
    mx_ln = 0
    for lt in range(0, n):
        sm = 0
        for rt in range(lt, n):
            sm += t[rt]
            if sm <= k:
                mx_ln = max(mx_ln, rt-lt+1)
    print(mx_ln)  # 108

def A3():
    mx_ln = 0
    for lt in range(0, n):  # 4_000_000 * 1_000
        sm = 0
        for rt in range(lt, n):
            sm += t[rt]
            if sm <= k:
                mx_ln = max(mx_ln, rt-lt+1)
            else:
                break
    print(mx_ln)  # 108

def A3_exp():
    mx_ln = 0
    for lt in range(0, n):  # 4_000_000 * 1_000
        if lt%1_000==0: print(lt)
        sm = 0
        for rt in range(lt, n):
            sm += t[rt]
            if sm <= k:
                mx_ln = max(mx_ln, rt-lt+1)
            else:
                break
    print(mx_ln)  # 108
    
# A1()
# A2()
# A3()
A3_exp()
"""
Определите непрерывный отрезок времени максимальной длины, 
в течение которого сумма осадков была не более K.
0 1 2 3 4
2 - 0 = 2 + 1
"""
def f(x):
    xP = 2 <= x <=10
    xQ = 6 <= x <=14
    return (1 <= int(xP)) or xQ

lst_A = []
for l in range(0, +19):
    for r in range(l+1, +20):
        lst_A.append([l, r])

for A in lst_A:
    if all(f(x) for x in range(A[0], A[1]+1)):
        print(A, A[1]-A[0]+1)

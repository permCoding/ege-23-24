def f(A, x):
    return (x&A == 0) or (x&37 != 0) or (x&12 != 0)

for A in range(10_000, 0, -1):
    if all(f(A,x) for x in range(1, 10_000)):
        print(A)
        break  # 45

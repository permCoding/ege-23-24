a, b = '09:51', '16:26'

h, m = map(int, a.split(':'))
v = h*60 + m

h, m = map(int, b.split(':'))
z = h*60 + m

r = z-v
print(f"{r//60}:{r%60}")

# z = 
mn = 500
for n in range(4, 500):
	b = bin(n)[2:]
	b += b[-3:] if n%3 == 0 else bin((n%3) * 3)[2:]
	r = int(b, 2)
	if 151 < r < mn: mn = r
print(mn)

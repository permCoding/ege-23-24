s = "abc"

s.ljust(8, '.')
s.rjust(8, '.')
s.center(8, '.')

s = str(1101)
print(s.zfill(10))  # добавить слева нули
print(f"s = {s:3s}")

x = 3.14159
print(f"x ={x:5.2f}")
y = int(x)
print(f"y ={y:5}")


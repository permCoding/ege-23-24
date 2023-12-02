s = "abc"

print(s.ljust(8, '.'))
print(s.rjust(8, '.'))
print(s.center(8, '.'))

s = str(1101)
print(s.zfill(10))  # добавить слева нули

print(f"s = {{ {s*2} }}")

print(f"s = {s*2}")
print(f"s = {s:3s}")

x = 3.14159
print(f"x ={x:5.2f}")

y = int(x)
print(f"y ={y:5d}")
print(f"y ={y:5}")

d = 123
b = ""

while d > 0:
    b += str(d % 10)
    d //=  10
    
print(b)

# print(d % 100)
num = int(input())

amount = 0
for div in range(1, num+1):
    if num % div == 0:
        amount += 1

if amount > 2:
    print(False)
else:
    print(True)
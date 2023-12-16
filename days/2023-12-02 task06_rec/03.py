f = open('./csv/table.csv')

nums = []
for line in f.readlines():
    nums.append([int(x) for x in line.split(' ')])
f.close()

size = len(nums)
d1, d2 = 0, 0
for i in range(size):
    d1 += nums[i][i]
    d2 += nums[size-1 - i][i]

print(f'{d1=} {d2=}')
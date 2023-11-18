s = "23;16;12;47;89;84"

sep = ";"

lst = s.split(sep)
print(lst)

nums = []
for elm in lst:
    nums.append(int(elm))
    # nums += [int(elm)]
print(nums)

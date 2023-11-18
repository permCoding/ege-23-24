s = "23;16;12;47;89;84"

sep = ";"

lst = s.split(sep)

# nums = [int(elm) for elm in lst]

def get(x): return x**2
nums = tuple(map(get, range(6)))

print(nums)

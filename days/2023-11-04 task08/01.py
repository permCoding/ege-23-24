import itertools as it

f = open("./01.py")
r = range(1, 4)
l = [1,2,3]
t = (1,2,3)
s = "123"

# for line in r: print(line)

for item in it.combinations(s, 2):
    print("".join(item))
print()
for item in it.permutations(s, 2):
    print("".join(item))
print()
for item in it.product(s, repeat=2):
    print("".join(item))

#    1  2  3  4
# 1 11 12 13 14
# 2 21
# 3
# 4          44
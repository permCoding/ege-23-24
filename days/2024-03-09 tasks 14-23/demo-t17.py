nums = [int(line) for line in open('./17_10100.txt')]
mx13 = max([num for num in nums if num%100==13])
# [num for num in nums if abs(num)%100==13]
# [num for num in nums if str(num)[-2:]=='13']

lst = []
for i in range(len(nums)-2):
    s = nums[i:i+3]
    u1 = (int(99<s[0]<=1000) + int(99<s[1]<=1000) + int(99<s[2]<=1000)) == 2
    u2 = sum(s) <= mx13
    if u1 and u2:
        lst.append(sum(s))

print(len(lst), max(lst))

for i, line in enumerate(open("./csv/09_9778.csv"), start=1):
    nums = [int(x) for x in line.split(';')]
    if len(set(nums)) == 5:
        np = [x for x in nums if nums.count(x)==1]
        y = sum(nums) - sum(set(nums))
        if y >= sum(np) / 4:
            print(i, nums)
            break

# lst = range(5)
# # lst = [12,34,56,78]
# for i, elm in enumerate(lst, start=1):
#     print(i, elm)

"""
повторяющееся число строки не меньше, 
чем среднее арифметическое четырёх её 
неповторяющихся чисел
[ if]
set
find
"""
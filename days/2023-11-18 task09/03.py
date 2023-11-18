i = 0
for line in open("./csv/09_9778.csv"):
    i += 1
    nums = [int(x) for x in line.split(';')]
    if len(set(nums)) == 5:
        np = [x for x in nums if nums.count(x)==1]
        y = [x for x in nums if nums.count(x)==2][0]
        if y >= sum(np) / 4:
            print(i, nums)
            break

"""
повторяющееся число строки не меньше, 
чем среднее арифметическое четырёх её 
неповторяющихся чисел
"""
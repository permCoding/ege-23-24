f = open("./26.txt")
n = int(f.readline())
lst = []
for line in f:
    lst.append(list(map(int, line.split())))

lst.sort(key=lambda x: x[1])  # print(lst)

filtred = []
end, pos = 0, 0
for i in range(n):
    if lst[i][0] >= end:
        end = lst[i][1]
        filtred.append(lst[i])
        pos = i
lst = sorted(lst[pos+1:], key=lambda x: x[0])

print(len(filtred), lst[-1][0], filtred[-2][1])
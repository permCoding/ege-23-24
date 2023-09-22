f = open("./26_10107.txt")
n = int(f.readline())
lst = [list(map(int, line.split())) for line in f]

lst.sort(key=lambda x: x[1])  # print(lst)

filtred = []
end, pos = 0, 0
for i in range(n):
    if lst[i][0] >= end:
        end = lst[i][1]
        filtred.append(lst[i])
        pos = i

lst = sorted(lst[pos:], key=lambda x: x[0])
print(len(filtred), lst[-1][0] - filtred[-2][1])
# жадный алгоритм ...
def solver_greedy():
    money.sort()
    right, sm = 0, 0
    while right < n:
        if sm + money[right] <= limit:
            sm += money[right]
        else:
            break
        right += 1
    cnt = right

    for i in range(right, n):
        if sm - money[right-1] + money[i] > limit:
            break
    return cnt, money[i-1]
    # last = money[right-1]
    # max_last = last
    # for elm in money[right:]:
    #     if sm - last + elm > limit:
    #         break
    #     else:
    #         max_last = elm
    # return cnt, max_last


f = open('./data/26_12256.txt')
limit, n = map(int, f.readline().split())
money = [int(line) for line in f]

# limit = 8
# money = [1, 2, 5, 4, 8, 10, 9]
print(solver_greedy())  # (629, 50)

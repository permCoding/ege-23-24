for line in open('./csv/table.csv').readlines():
    t = line.split()
    s = ""
    for elm in t:
        s += f"{elm:>6}"
    print(s)

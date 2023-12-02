for line in open('./csv/table.csv').readlines():
    t = line.split()
    # print(t[0].rjust(5, " "))
    # print(f"{t[0]:<5}")
    print(f"{t[0]:^5}")
    

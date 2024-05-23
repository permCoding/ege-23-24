for n in range(1917, 10**10+1, 1917):
    s = str(n)
    if s[0]=='3' and s[2:4]=='12' and s[5:7]=='14' and s[-1]=='5':
        print(n, n//1917)  # 3?12?14*5

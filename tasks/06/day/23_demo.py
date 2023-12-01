def get(n, m):
    if n==11 or n>m: return 0
    if n==m: return 1
    return get(n+1, m) + get(n*2, m) + get(n*n, m)

print(get(2, 20))  # 37

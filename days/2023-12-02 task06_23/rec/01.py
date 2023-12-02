def get(n):
    if n == 0: return 0  # точка останова
    return get(n-1) + n  # шаг рекурсии
    
print(get(10))

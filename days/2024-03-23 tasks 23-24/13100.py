s = open('./13100.txt').readline()

kc = kd = 0
gl, mx = 0, 0
for gr in range(len(s)):
    if s[gr] == 'C': kc += 1
    if s[gr] == 'D': kd += 1
    while kc > 2 or kd > 2:
        if s[gl] == 'C': kc -= 1
        if s[gl] == 'D': kd -= 1
        gl += 1
    if kc == 2 and kd == 2: 
        mx = max(mx, gr-gl+1)
print(mx)

"""
Текстовый файл содержит только 
заглавные буквы латинского алфавита (ABC…Z)

Определите максимальное количество идущих 
подряд символов, среди которых каждая 
из букв C и D встречается не более двух раз
"""
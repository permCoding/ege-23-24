s = open('./24_10724.txt').readline()
al = '0123456789ABCDEF'

mx_len, cr_len = 0, 0
for i in range(len(s)):
    if s[i] in al:
        if cr_len == 0 and s[i] == '0': continue
        cr_len += 1
        mx_len = max(mx_len, cr_len)
    else:
        cr_len = 0
print(mx_len)

"""
файл состоит из символов, обозначающих заглавные буквы латинского алфавита и цифры от 0 до 9 включительно. Определите максимальное количество идущих подряд символов, которые могут представлять запись числа в шестнадцатеричной системе счисления.

Числа с незначащими нулями в ответ брать не следует.
12ACEF

"""
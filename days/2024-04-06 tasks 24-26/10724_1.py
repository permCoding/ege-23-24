s = open('./24_10724.txt').readline()
al = '0123456789ABCDEF'

nums16, cr = [], ''
for i in range(len(s)):
    if s[i] in al:
        cr += s[i]
    else:
        for j in range(len(cr)):
            if cr[j] != '0':
                break
        if cr[j:] != '': nums16.append(cr[j:])
        cr = ''

# max_len = 0
# for num in nums16:
#     max_len = max(max_len, len(num))
# print(max_len)


res = max(nums16, key=len)
print( len(res) )

"""
файл состоит из символов, обозначающих заглавные буквы латинского алфавита и цифры от 0 до 9 включительно. Определите максимальное количество идущих подряд символов, которые могут представлять запись числа в шестнадцатеричной системе счисления.

Числа с незначащими нулями в ответ брать не следует.
0000012ACEF
120F
AF
FFFFF
0000000000000017uiseyfvwuecvweu34343skldhcbsdjhkAAD
"""
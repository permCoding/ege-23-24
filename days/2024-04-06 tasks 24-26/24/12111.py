s = open('./24_12111.txt').readline()
# s = 'JNYNPNYNOKLMHPYHPYHPYLKNLHPJJNHPY'

s = s.replace('HPY', '.').replace('NYN', '.')

n = 1
while s.find( '.'*n ) >= 0:
    n += 1
print( n-1 )

# for n in range(1, 10**3):
#     if s.find('.' * n) < 0:
#         print( n-1 )
#         break
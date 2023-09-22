import os


os.system("cls||clear")

for N in range(1, 100):
    b = bin(N)[2:]
    if b.count('1') % 2 == 0:
        R = '10' + b[2:] + '0'
    else:
        R = '11' + b[2:] + '1'
    print(R, int(R, 2))
    if int(R, 2) > 40:
        print(N)
        break

'''
На вход алгоритма подаётся натуральное число N. 
Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. Далее эта запись обрабатывается по следующему правилу:
  а) если сумма цифр в двоичной записи числа чётная, то к этой записи
  справа дописывается 0, а затем два левых разряда заменяются на 10;
  б) если сумма цифр в двоичной записи числа нечётная, то к этой записи
  справа дописывается 1, а затем два левых разряда заменяются на 11.
Полученная таким образом запись является двоичной записью искомого
числа R.

Например, для исходного числа 6(10) = 110(2) результатом является число
1000(2) = 8(10), а для исходного числа 4(10) = 100(2) результатом является число
1101(2) = 13(10).

Укажите минимальное число N, после обработки которого с помощью
этого алгоритма получается число R, большее 40. В ответе запишите это
число в десятичной системе счисления.
'''
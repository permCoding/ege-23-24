# id = 60 * ______ byte ?
#al = '012u39xuhoqwdidbqwesgfhb08iwqebqoiw'  # 260
cnt_bit = 9  # bit 512 >= 260
id = 60 * cnt_bit / 8  # byte
print(id)

id = 68  # byte
v = 65_536 * id / 1_024
print(v)  # 4352


"""
al = '01'    # 1 -> 0 1
al = '0123'  # 2
al = '01234' # 3

000 == 0
001 == 1
010 == 2
011 == 3
100 == 4

101 == 5
110 == 6
111 == 7
"""
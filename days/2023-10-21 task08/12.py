def to_dec(b, exp=0):
    if b == "":
        return 0
    else:
        return int(b[-1]) * 2**exp + to_dec(b[:-1], exp+1)


b = "1101"
print(to_dec(b))

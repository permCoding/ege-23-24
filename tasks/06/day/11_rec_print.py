def get(f, count):
    if count == 0:
        print('= '*9)
    else:
        print(next(f).rstrip())
        get(f, count-1)

f = open("./11_rec_print.py")
get(f, 5)

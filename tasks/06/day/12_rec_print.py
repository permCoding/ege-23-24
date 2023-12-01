def get(f):
    try:
        print(next(f).rstrip())
        get(f)
    except:
        pass

f = open("./12_rec_print.py")
get(f)

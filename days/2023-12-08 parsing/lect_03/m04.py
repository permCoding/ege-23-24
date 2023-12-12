def get_mins(s):
    h, m = map(int, s.split(':'))
    return h*60 + m


def get_day_len(a, b):
    v, z = get_mins(a), get_mins(b)
    r = z-v
    return f"{str(r//60).zfill(2)}:{r%60}"

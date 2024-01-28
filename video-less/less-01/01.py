import re


def check_a(pin):
    try:
        dec = int(pin, 10)
        # return True if 999 < dec < 10000 else False
        return 999 < dec < 10000
    except:
        return False


def check_b(pin):
    if len(pin) == 4 and all(smb in '0123456789' for smb in pin):
        return True
    else:
        return False


def check_c(pin):
    # ptn = '^....$'
    # ptn = '^[0123456789][0123456789][0123456789][0123456789]$'
    # ptn = '^[0-9][0-9][0-9][0-9]$'
    
    # ptn = '^[0-9]{4}$'
    # ptn = '^\\d\\d\\d\\d$'  # \n \b \t \r
    # ptn = '^\\d{4}$'
    # ptn = '\\d{4}$'
    # ptn = '\\d{4}'
    ptn = r'^\d{4}$'
    
    # res = re.match(ptn, pin)  # начинается с шаблона
    res = re.search(ptn, pin)  # шаблон есть в строке
    print(res)
    return True if res else False


pin = input("enter pin - ")
print(check_c(pin))

import re


def is_password(pin):
    # ptn = r'^[A-Za-z0-9]{4,8}$'
    ptn = r'^\w{4,8}$'
    ptn = r'^[-\w]{4,8}$'
    res = re.search(ptn, pin)
    return True if res else False


while True:
    psw = input("enter password - ")
    if is_password(psw):
        break

print('Success psw')

# Ёё

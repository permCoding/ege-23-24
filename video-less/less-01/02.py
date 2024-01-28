import re

def is_pin(pin):
    ptn = r'^\d{4}$'
    res = re.search(ptn, pin)
    return True if res else False


while True:
    pin = input("enter pin (4 digits) - ")
    if is_pin(pin):
        break

print('Success pin')

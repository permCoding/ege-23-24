from ipaddress import *

def check(ip):
    return f'{ip:b}'[16:].count('1') > 3

for A in range(256):
    if all(check(ip) for ip in ip_network(f'183.192.{A}.0/255.255.252.0', 0)):
        print(A)
        break

"""
минимальное значение А
суммарное количество единиц 
в правых двух байтах больше трёх
"""
# for ad in ip_network(ip, 0):
#     if '101' not in f'{ip_address(ad):b}':
#         cnt += 1



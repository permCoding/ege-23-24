from ipaddress import *


# ip = '136.36.240.16/255.255.255.248'
ip = '136.36.240.16/29'  # .11111000

cnt = 0
for ad in ip_network(ip, 0):
    if '101' not in f'{ip_address(ad):b}':
        cnt += 1

print(cnt)

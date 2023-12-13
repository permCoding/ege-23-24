import re

s = '<div>111</div><div>333</div>'

p = '<div>(\w+?)</div>$'

t = re.findall(p, s)

print(t)

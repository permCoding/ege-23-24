import re

s = '<div>111</div>\n<div>333</div><div>555</div>'

p = '^<div>(\w+?)<'

# t = re.findall(p, s)
t = re.findall(p, s, re.MULTILINE)

print(t)

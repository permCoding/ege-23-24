import re

s = '<div>111<span>222</span>333</span></'

p = '\W+'
p = '[^A-Za-z0-9_]{2,}'

t = re.findall(p, s)

print(t)

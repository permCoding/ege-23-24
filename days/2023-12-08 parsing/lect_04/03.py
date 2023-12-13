import re

s = '7ABA 123 BA 44 B660874A     9D'

p = '([^0-9\s][0-9]+)'

t = re.findall(p, s)

print(t)

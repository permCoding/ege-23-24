import re

s = 'Почка почка Полка полка пот Потоп'

p = 'по\w*'

t = re.findall(p, s, re.IGNORECASE)

print(t)

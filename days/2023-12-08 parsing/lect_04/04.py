import re

s = '<div>111<span>222</span>333</span></'

p = '<span>.*?</'
p = '<span>(.*?)</'

t = re.findall(p, s)

print(t)

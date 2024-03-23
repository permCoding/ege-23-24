s = open('./10105.txt').readline()

gl, gr = 0, 0
mx, cr = 0, 0

while gr < len(s):
    if s[gr] == 'T': cr += 1
    while cr > 100:
        if s[gl] == 'T': cr -= 1
        gl += 1
    if cr == 100: mx = max(mx, gr-gl+1)
    gr += 1

print(mx)

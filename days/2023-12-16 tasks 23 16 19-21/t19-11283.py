def check(step, t):
    if step in [1,3]: return all(t)
    return any(t)

def game(a,b,step):
    if a+b>=342: return step in [2,4]
    if step == 4: return False
    step += 1
    t = [
        game(a+2,b,step),
        game(a,b+2,step),
        game(a*5,b,step),
        game(a,b*5,step)
    ]
    return check(step, t)

for s in range(1, 326):
    if game(11,s,0): print(s)

# https://kompege.ru/task
# 19 => 14
# 20 => 57 64
# 21 => 65
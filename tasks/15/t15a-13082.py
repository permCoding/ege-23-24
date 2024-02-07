def f(x, y, A):
    return (3*x+y>48) or (x>y) or (4*x+y<A) 


for A in range(1, 100):
    if any(f(x,y,A)==False for x in range(1,100) for y in range(1,100)):
        print(A)
        # break

"""
При каком наибольшем целом A найдутся такие целые неотрицательные x и y, что выражение
(3x+y>48)∨(x>y)∨(4x+y<A)        будет ложным?
"""
# f = open('./27-A.txt')
f = open('./27-B.txt')  # 10**6
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mx_abc = -float('inf')

pairs = [i for i in range(0, n-2*k)]  # 2*k

t_a = [(t[a], a) for a in range(0, n)]
t_a.sort(reverse=True)  # n*log(n) => 20 млн
t_a = list(map(lambda x: x[1], t_a))

for b in range(0, n-2*k):
    c = b + 2*k
    for a in t_a:
        if a!=b and a!=c:
            mx_abc = max(mx_abc, t[a]+t[b]+t[c])
            break

print(mx_abc)  # 205706  23894 => 6 sec

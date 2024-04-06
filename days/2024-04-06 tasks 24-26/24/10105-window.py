s = open('./24_10105.txt').readline()

diap = 100

# s = 'T' + '...T..T.TT.T......T..' + 'T'

all_pos_T, start = [], 0
while s.find('T', start) > -1:
    pos_T = s.find('T', start)
    all_pos_T.append(pos_T)
    start = pos_T + 1

lns = []
for pos in range(0, len(all_pos_T)-diap-1):
    lns.append( all_pos_T[pos+diap+1] - all_pos_T[pos] - 1 )

print(max(lns))

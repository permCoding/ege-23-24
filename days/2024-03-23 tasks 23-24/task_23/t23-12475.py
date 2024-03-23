def f1(cur, step):
    if step == 68:
        st.add(cur)
    else:
        f1(cur+3, step+1)
        f1(cur-2, step+1)


from functools import lru_cache
@lru_cache()
def f2(cur, step):
    if step == 68:
        st.add(cur)
    else:
        f2(cur+3, step+1)
        f2(cur-2, step+1)


def f3(cur, step):
    if step == 68:
        st.add(cur)
    else:
        for elm in [cur+3, cur-2]:
            if (elm, step+1) not in cache:
                f3(elm, step+1)
                cache.add((elm, step+1))


cache = set()  # множество пар
st = set()
start, step = 1, 0
f3(start, step)

print(st)
print(len(st))

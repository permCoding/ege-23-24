def get_key(elm):
    return len(elm)


def get_lines(filename):
    with open(filename) as f:
        return f.readlines()


lines = get_lines('./data/lang_rate.txt')
langs = [line.strip().split(";")[1] for line in lines]

for i, lang in enumerate(sorted(langs, key=get_key), start=1):
    print(f"{i};{lang}")

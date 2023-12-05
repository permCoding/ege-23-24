def get_key(elm):
    return len(elm)


def get_lines(filename):
    with open(filename) as f:
        return f.readlines()


def to_file(filename, langs):
    with open(filename, "w") as f:
        for i, lang in enumerate(sorted(langs, key=get_key), start=1):
            line = f"{i};{lang}\n"
            f.write(line)


lines = get_lines('./data/lang_rate.txt')
langs = [line.strip().split(";")[1] for line in lines]
to_file("./data/langs.txt", langs)

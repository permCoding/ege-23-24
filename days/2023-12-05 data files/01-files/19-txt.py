def get_lines(filename):
    with open(filename) as f:
        return f.readlines()


def to_file(filename, langs):
    with open(filename, "w") as f:
        lst = sorted(langs, key=lambda elm: len(elm))
        lines = [f"{i+1};{elm}\n" for i, elm in enumerate(lst)]
        f.writelines(lines)


lines = get_lines('./data/lang_rate.txt')
langs = [line.strip().split(";")[1] for line in lines]
to_file("./data/langs.txt", langs)

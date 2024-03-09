al = "0123456789abcdefghi"

for x in al:
    op1 = int(f"98897{x}21", 19)
    op2 = int(f"2{x}923", 19)
    res = op1 + op2
    if res % 18 == 0:
        print(x, res // 18)


# int(s, 19)
# 98897x21(19) + 2x923(19)

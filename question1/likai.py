def x(s):
    for i in range(0, len(s)):
        print(s[i] * (i + 1), end="")
    if len(s) > 1:
        print()
        return x(s[1:])
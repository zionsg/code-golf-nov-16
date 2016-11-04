def f(s, c):
    s += ' ' * (-len(s) % c)
    e = ''
    for d in range(c):
        e += s[d::c]
    return e
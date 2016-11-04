
def r(s,k):
    while len(s) % k:
        s += ' '
    l = len(s)
    o = ''
    for c in range(k):
        i = c
        while i < l:
            o += s[i]
            i += k
    return o


def r(s,k):
    while len(s) % k:
        s += ' '
    o = ''
    for c in range(k):
        i = c
        while i < len(s):
            o += s[i]
            i += k
    return o

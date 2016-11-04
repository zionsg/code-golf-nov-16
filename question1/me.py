def z(a):
    c = ""
    r=range
    l=len
    for i in r(l(a)):
        b = a[i:]
        c += (''.join(b[i] * (i+1) for i in r(l(b)))) + "\n"
    return c

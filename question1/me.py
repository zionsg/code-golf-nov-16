def z(a):
    c = ""
    r=range
    l=len
    for i in r(len(a)):
        b = a[i:]
        c += (''.join(b[i] * (i+1) for i in range(len(b)))) + "\n"
    return c

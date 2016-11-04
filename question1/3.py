def j(i):
    o = []
    def a(i, o):
        o +=  [i]
        if i == 1:
            return
        if i%2:
            a(int(pow(i,1.5)), o)
        else:
            a(int(pow(i,0.5)), o)
    a(i, o)
    return o

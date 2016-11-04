def j(i):
    o = [i]
    while i > 1:
        if i%2:
            o += [int(pow(i,1.5))]
        else:
            o += [int(pow(i,0.5))]
        i = o[-1]
    return o

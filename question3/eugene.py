def a(k):
    b = a(k-1)
    if b % 2 == 0:
        return int(b**.5)
    else:
        return int(b**1.5)

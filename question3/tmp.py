def g(n):
    print n,
    if n == 1:
        return
    g(int(n**.5)) if n%2 == 0 else g(int(n**1.5))

g(3) 67 chars

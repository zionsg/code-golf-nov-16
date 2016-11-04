def f(s,n):
    for t in zip(*[list(s[i:i+n])+['']*(n-len(s[i:i+n])) for i in range(0,len(s),n)]):
        print "".join(t),
# 101 chars


def x(s, i):
    if i == len(s):
        return []
    else:
        a=x(s,i+1)
        return a + [s[i-1],s[i+1]] if s[i] == 0 else a

r = lambda s: max(x(s, 0))
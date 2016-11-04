
def z(a):
    b = [1] + a
    c = a[1:] + [1]
    return max(a[i] for i in range(len(a)) if c[i] == 0 or b[i] == 0)

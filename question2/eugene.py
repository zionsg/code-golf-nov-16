#from functionals import map
def a(b):
    i = list(map(int, b.split())).index(0)
    print(i)
    r = b[i+1] 
    l = b[max(i-1,0)]
    print(r, l)

print(a("1 4 3 6 0 3 7 0"))
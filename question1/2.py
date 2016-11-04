def z(a): return max(a[i] for i in range(len(a)) if (a[1:]+[1])[i] == 0 or ([1]+a)[i] == 0)

s=input()

def z(s):
    r=''
    for i,c in enumerate(s):
        r+=(i+1)*c
    return r

for i in range(len(s)):
    print(z(s[i:]))

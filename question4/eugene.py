def f(s,k):
    r = ''
    for i in range(k):
        _ = ' ' if i % k else ''
        r += s[i::k] + _
    return r

print(f('codegolf.stackexchange.com', 4))
def uses_only(s,x):
    F=True
    for c in s:
        if c in x:
            F=F and x.find(c)
    return F
s="asdfg"
x='sdfga'
print(uses_only(s,x))


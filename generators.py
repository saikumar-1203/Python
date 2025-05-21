def gen():
    l=[5,10,15,20]
    for p in l:
        yield p
g=gen()
for p in g:
    print(p,end=" ")

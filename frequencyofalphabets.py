n=input().strip()
d={}
for p in n:
    if p not in d:
        d[p]=1
    else:
        d[p]+=1
l=[]
for p,q in d.items():
    l.append(p)
    l.append(q)
for p in l:
    print(p,end="")
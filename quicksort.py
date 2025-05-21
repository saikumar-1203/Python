def quick(l):
    if (len(l)<=0):
        return l
    else:
        pi=l.pop()
        less=[]
        more=[]
        for p in l:
            if(p<pi):
                less.append(p)
            else:
                more.append(p)
        d=quick(less)+[pi]+quick(more)
        return d
l=list(map(int,input().split()))
print("Before sort",l)
i=quick(l)
print("After insertion",i)
def insertion(l):
    for p in range(1,len(l)):
        temp=l[p]
        q=p-1
        while(q>=0) and (temp<l[q]):
            l[q+1]=l[q]
            q=q-1
        l[q+1]=temp
    return l
l=list(map(int,input().split()))
print("Before sort",l)
i=insertion(l)
print("After insertion",i)
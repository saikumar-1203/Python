def merged(left,right):
    m=[]
    l=0
    r=0
    while(l<len(left) and r<len(right)):
        if(left[l]<right[r]):
            m.append(left[l])
            l+=1
        else:
            m.append(right[r])
            r+=1
    m+=left[l:]+right[r:]
    return m
def mergesort(l):
    m=len(l)//2
    if(len(l)<=1):
        return l
    else:
        left=mergesort(l[:m])
        right=mergesort(l[m:])
        return merged(left,right)   
    # d=merged(left,right)
    # return d
l=list(map(int,input().split()))
print(l)
m=mergesort(l)
print(m)
def binary(l,key):
    left=0
    right=len(l)-1
    while(left<=right):
        mid=(left+right)//2
        if (key==l[mid]):
            return mid
        elif (key<l[mid]):
            right=mid-1
        else:
            left=mid+1
    return -1
l=list(map(int,input().split()))
l.sort()
key=int(input())
b=binary(l,key)
if (b==-1):
    print("element not found")
else:
    print("element found at",b,"location")

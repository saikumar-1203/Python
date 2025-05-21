def linear(l,key):
    for p in range(len(l)):
        if l[p]==key:
            return p
    return -1

l=list(map(int,input().split()))
key=int(input())
b=linear(l,key)
if (b==-1):
    print("element not found")
else:
    print("element found at",b,"location")
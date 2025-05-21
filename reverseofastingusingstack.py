inp=input("enter the string")
l=[]
r=""
for p in range(len(inp)):
    l.append(inp[p])
print(*l)
for p in range(len(l)):
    r=r+l.pop()
print(r)
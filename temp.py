n=input()
n=list(n)
r=""
for i in range (len(n)):
    r+=n.pop()
print(r)
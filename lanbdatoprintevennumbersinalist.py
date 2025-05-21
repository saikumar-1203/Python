l=[1,2,3,4,5,6,7,8]
s=lambda n:n%2!=0
r=[p for p in l if s(p)]
print("odd numbers:")
print(*r)
s=lambda n:n%2==0
r=[p for p in l if s(p)]
print("Even numbers:")
print(*r)
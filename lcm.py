a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if a>b: 
    max=a
else:
    max=b
lcm=max
while(lcm%a!=0 | lcm%b!=0):
    lcm+=max
print(lcm)
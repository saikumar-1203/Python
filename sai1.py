a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
small=min(a,b)
big=max(a,b)
while(True):
    if(a%big==0 and b%big==0):
        print(big)
    else:
        big+=1
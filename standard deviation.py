import math 
x=input("Enter data:")
n1,n2,n3,n4,n5,n6=x.split(" ")
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
n6=int(n6)
mean=(n1+n2+n3+n4+n5+n6)/6
deviation=(((n1-mean)**2)+((n2-mean)**2)+((n3-mean)**2)+((n4-mean)**2)+((n5-mean)**2)+((n6-mean)**2))/5
standard_deviation=(math.sqrt(deviation))
print(standard_deviation)
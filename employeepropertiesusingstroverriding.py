class employee:
    def __init__(self,name,id,salary):
        self.ename=name
        self.eid=id
        self.esalary=salary
    def __str__(self):
        return self.ename+" "+str(self.eid)+" "+str(self.esalary)
s=employee("joy",401,50000)
print(s)
s1=employee("jaysree",402,35000)
print(s1)
s2=employee("ramesh",403,30000)
print(s2)
s3=employee("suresh",404,30000)
print(s3)
s4=employee("rajesh",405,20000)
print(s4)
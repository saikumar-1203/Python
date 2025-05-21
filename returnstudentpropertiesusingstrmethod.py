class student():
    def __init__(self,name,id,add):
        self.name=name
        self.id=id
        self.add=add
    def __str__(self):
        return self.name,self.id,self.add
        
x1=student("sai",24,"hyd")
r=x1.__str__()
print(*r)
x2=student("raju",45,"kadapa")
r=x2.__str__()
print(*r)

class teacher():
    def __init__(self,tname,tid,tadd):
        self.tname=tname
        self.tid=tid
        self.tadd=tadd
    def __str__(self):
        return self.tname+" "+str(self.tid)+" "+self.tadd
t1=teacher("ravi",456,"tirupati")
print(t1)
t2=teacher("ramesh",478,"chittor")
print(t2)
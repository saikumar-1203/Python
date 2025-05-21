class student():
    def insert(self,name,rno,marks):
        self.name=name
        self.rno=rno
        self.marks=marks
    def display(self):
        print(self.name,self.rno,self.marks)
class employee():
    def update(s,m):
        s.marks=m
        s.display()
class faculty():
    def insert1(self,fname,fsalary):
        self.name1=fname
        self.salary=fsalary
    def display1(self):
        print(self.fname1,self.fsalary)
class manageent():
    def update1(u,us):
        u.fsalary=us
        u.display1()

s1=student()
s1.insert("Raju",484,75)
s1.display()
employee.update(s1,95)
s2=faculty()
s2.insert1("ramu",40000)
s2.display1()

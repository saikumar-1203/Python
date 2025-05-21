class parent:
    def insert(self):
        self.name=input("enter the name")
        self.rno=int(input("enter the roll no"))
        self.add=input("enter the address")
class mba(parent):
    def insert1(self):
        self.insert()
        self.s1=input("enter sub1")
        self.s2=input("enter sub2")
        self.s3=input("enter sub2")
    def stu_info(self):
        print(self.name,self.rno,self.add,self.s1,self.s2,self.s3)
class mca(parent):
    def insert1(self):
        self.insert()
        self.s1=input("enter sub1")
        self.s2=input("enter sub2")
        self.s3=input("enter sub2")
    def stu_info(self):
        print(self.name,self.rno,self.add,self.s1,self.s2,self.s3)
s1=mba()
s2=mca()
s1.insert1()
s1.stu_info()
s2.insert1()
s2.stu_info()

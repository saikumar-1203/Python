class person:
    def insert(self):
        self.name=input("enrter the name")
        self.address=input("enter address")
class student(person):
    def insert1(self):
        self.insert()
        self.rno=int(input("enter roll no"))
        self.marks=int(input("enter marks"))
    def stu_info(self):
        print(self.name,self.rno,self.marks,self.address)
s1=student()
s1.insert1()
s1.stu_info()
        







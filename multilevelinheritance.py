class person:
    def insert(self):
        self.name=input("enrter the name")
        self.address=input("enter address")
class employee(person):
    def insert1(self):
        self.eid=int(input("enter roll no"))
        self.experience=int(input("enter marks"))
class semployee(employee):
    def insert2(self):
        self.insert()
        self.insert1()
        self.salary=int(input("enter the salary"))
    def emp_info(self):
        print(self.name,self.address,self.eid,self.experience,self.salary)
s1=semployee()
s1.insert2()
s1.emp_info()
        







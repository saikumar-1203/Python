class x:
    a=100
    def insert(self):
        self.b=300
    def m1(self):
        print("in m1")
class y:
    c=400
    def insert1(self):
        self.d=500
    def m2(self):
        print("in m2")
    def display(self):
        print(y.c)
        self.insert1()
        print(self.d)
        self.m2()
        x1=x()
        print(x1.a)
        x1.insert()
        print(x1.b)
        x1.m1()
y1=y()
y1.display()

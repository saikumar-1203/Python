class rectangle():
    def insert(self):
        self.l=int(input("Enter the length"))
        self.b=int(input("Enter the bredth"))
    def area(self):
        a=self.l*self.b
        print("The area of rectangle is ",a)
t=rectangle()
t.insert()
t.area()
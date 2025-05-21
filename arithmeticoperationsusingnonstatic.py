class calc:
    def insert(self):
        self.a=20
        self.b=10
    def add(self):
        print("sum",self.a+self.b)
    def sub(self):
        print("diff",self.a-self.b)
    def mul(self):
        print("product",self.a*self.b)
    def div(self):
        print("div",self.a//self.b)
t1=calc()
t1.insert()
t1.add()
t1.sub()
t1.mul()
t1.div()
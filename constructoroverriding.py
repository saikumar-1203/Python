class x:
    def __init__(self,x):
        self.x=x
        print("the square of the number:",self.x*self.x)
class y(x):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("The sum is:",self.a+self.b)
        super().__init__(a)
y1=y(20,10)
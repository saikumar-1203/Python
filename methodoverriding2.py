class x:
    def __init__(self,x):
        self.x=x
        
    def __str__(self):
        return self.x
x1=x("python")
r=x1.__str__()
print(r)
x2=x("java")
r=x2.__str__()
print(r)
x3=x("c++")
r=x3.__str__()
print(r)
x4=x("c")
r=x4.__str__()
print(r)
x5=x("r")
r=x5.__str__()
print(r)
x6=x("Java")
r=x6.__str__()
print(r)
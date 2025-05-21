class x:
    def m1(self):
        print("in m1 of x")
    def m2(self):
        print("in m2 of x")
class y(x):
    def m3(self):
        print("in m3 of y")
    def m2(self):
        print("in m2 of y")
y1=y()
y1.m1()
y1.m2()
y1.m3()
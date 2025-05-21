class student():
    cname="NRCM"
    def __init__(self,name,rno,s1,s2,s3):
        self.name=name
        self.rno=rno
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def stu(self):
        print(self.name,self.rno,self.s1,self.s2,self.s3)
    def check(self):
        if(self.s1>35 and self.s2>35 and self.s3>35):
            print(self.name+" is pass.")
        else:
            print(self.name+" is fail.")
n=int(input("Enter the no of students:"))
i=1
while (i<=n):
    name=input("enter the name:")
    rno=int(input("Enter the roll no:"))
    s1,s2,s3=map(int,input("enter the 3 subject marks:").split())
    st=student(name,rno,s1,s2,s3)
    st.stu()
    st.check()
    i+=1


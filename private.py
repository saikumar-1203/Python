class person:                                   #private
    def insert(self,name,add):
        self.__name=name
        self.__add=add
        print(self.__name,self.__add)
class student(person):
    def __init__(self,rno,marks):
        self.__rno=rno
        self.__marks=marks
    def __stu_info(self):
        print(self.__rno,self.__marks)
    def stu_info(self):
        self._stu_info()
s1=student(420,100)
s1.insert("sai","ylr")
s1.stu_info()
print(s1._student__name)
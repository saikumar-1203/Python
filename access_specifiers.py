#class student:
#     def insert(self,name,rno,marks):                 public
#         self.name=name
#         self.rno=rno
#         self.marks=marks
#     def stu_info(self):
#         print(self.name,self.rno,self.marks)
# s1=student()
# s1.insert("sai kumar",484,1000)
# s1.stu_info()
# print(s1.name)
# print(s1.rno)
# print(s1.marks)



# class person:                    #protected
#     def insert(self,name,add):
#         self._name=name
#         self._add=add
# class student(person):
#     def __init__(self,rno,marks):
#         self._rno=rno
#         self._marks=marks
#     def stu_info(self):
#         print(self._rno,self._marks)
# s1=student(420,100)
# s1.insert("sai","ylr")
# s1.stu_info()
# print(s1._name)
class person:                                   #private
    def insert(self,name,add):
        self.__name=name
        self.__add=add
        print(self.__name,self.__add)
class student(person):
    def __init__(self,rno,marks):
        self.__rno=rno
        self.__marks=marks
    def stu_info(self):
        print(self.__rno,self.__marks)
s1=student(420,100)
s1.insert("sai","ylr")
s1.stu_info()
#print(s1.__name)   # we cannot access due to presence of function outside the class.
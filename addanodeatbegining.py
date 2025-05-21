class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class single:
    def __init_(self):
        self.head=None
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    def begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
s1.begining(50)
s1.display()
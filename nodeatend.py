class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init_(self):
        self.head=None
    def end(self,data):
        temp=self.head
        while(temp.next):
            temp=temp.next
        nb=Node(data)
        temp.next=nb
    def middle(self,loc,data):
        temp=self.head
        for i in range(loc):
            temp=temp.next
        nb=Node(data)
        temp.next=nb
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.end(50)
s1.display()

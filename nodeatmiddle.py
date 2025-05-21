class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init_(self):
        self.head=None
    def begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def middle(self,loc,data):
        if loc==1:
            self.begining(data)
        else:
            temp=self.head
            for i in range(1,loc-1):
                temp=temp.next
            nb=Node(data)
            nb.next=temp.next
            temp.next=nb
            while(temp.next):
                temp=temp.next

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
s1.middle(1,90)
s1.display()

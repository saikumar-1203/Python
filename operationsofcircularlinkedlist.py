class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cir:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self):
        n=int(input("Enter nmber of nodes"))
        for p in range(n):
            data=int(input("Enter data:"))
            nb=Node(data)
            if self.head==None:
                self.head=nb
                self.tail=nb
                self.tail.next=self.head
            else:
                self.tail.next=nb
                self.tail=nb
                self.tail.next=self.head
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
            if(temp==self.head):
                break
        print(temp.data)

c1=cir()
c1.insert()            
c1.display()

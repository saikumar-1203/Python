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
    def add_beg(self,data):
        nb=Node(data)
        self.tail.next=nb
        nb.next=self.head
        self.head=nb
    def add_end(self,data):
        nb=Node(data)
        self.tail.next=nb
        nb.next=self.head
        self.tail=nb
    def del_beg(self):
        self.head=self.head.next
        self.tail.next=self.head
    def del_end(self):
        temp=self.head
        while(temp.next!=self.tail):
            temp=temp.next
        temp.next=self.head
        self.tail=temp
    def print_position_data(self,loc):
        temp=self.head
        i=1
        while(temp):
            if i==loc:
                print(temp.data)
                break
            else:
                i+=1
                temp=temp.next
    def count(self):
        temp=self.head
        c=1
        while temp.next!=self.head:
            temp=temp.next
            c+=1
        print(c)



           
c1=cir()
c1.insert()            
c1.display()
c1.add_beg(80)
c1.display()
c1.add_end(90)
c1.display()
c1.del_beg()
c1.display()
c1.del_end()
c1.display()
c1.print_position_data(3)
c1.count()


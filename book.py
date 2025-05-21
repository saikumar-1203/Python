class book():
    def __init__(self,name,cost,pages):
        self.name=name
        self.cost=cost
        self.pages=pages
    def print1(self):
        print("Name:",self.name)
        print("cost:",self.cost)
        print("pages:",self.pages)    
n=int(input("Enter the  no of books:"))
while(n>0):
    name=input("Enter the book name:")
    cost=int(input("Enter the cost:"))
    pages=int(input("Enter the pages:"))
    t=book(name,cost,pages)
    t.print1()
    n-=1

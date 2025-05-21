class temp():
    def __init__(self):
        self.s=input("Enter the string")
    def rev(self):
        r=""
        l=len(self.s)-1
        while(l>=0):
            r+=self.s[l]
            l-=1
        print("reverse",r)
t=temp()
t.rev()
    
    
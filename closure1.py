def display(ch):
    def dis(n):
        print(ch*n)
    return dis
d=display("*")
d(10)
d1=display("@")
d1(10)
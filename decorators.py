def newdis(d):
    def gnew():
        print("*"*20)
        d()
        print("*"*20)
    return gnew
@newdis
def display():
    print("Python Programming")
display()
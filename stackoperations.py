size = int(input("Enter the size: "))
top=-1
l=[]
def push():
    global top
    if (top < size-1):
        top+=1
        ele=int(input())
        l.append(ele)
    else:
        print("stack is overflow")
def display():
    if top==-1:
        print("stack is empty")
    else:
        for p in range(len(l)-1,-1,-1):
            print(l[p])
def pop():
    global top
    if top==-1:
        print("top is empty")
    else:
        ele=l.pop()
        print("del:",ele)
        top-=1
def peek():
    global top
    if top==-1:
        print("stack is empty")
    else:
        print("the top element is:",l[-1])
while(True):
    print("1.push\n2.pop\n3.display\n4.peek\n5.exit")
    opt=int(input())
    match(opt):
        case 1: push()
        case 2: pop()
        case 3: display()
        case 4: peek()
        case 5: break



    
        


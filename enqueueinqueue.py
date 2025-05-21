front=-1
rear=-1
size=int(input("Enter the size:"))
q=[]
def enqueue():
    global front,rear
    if (rear==size-1):
        print('"queue is full')
    else:
        if front==-1:
            front=0
        rear+=1
        ele=int(input("enter the element"))
        q.append(ele)
def display():
    if (front == -1):
        print("queue is empty.")
    else:
        for p in range (len(q)):
            print(q[p],end=" ")
def dequeue():
    global rear,front
    if (front==-1):
        print("Queue is empty")
    elif (front!=rear):
        print("The deleted element is :",q.pop())
        front=-1
        rear=-1
    else:
        print("Top element is :"q[0])
def peek():
    if (front==-1):
        print("Queue is empty.")
    else:
        print("Top element is ",q[0])
while(True):
    print("1.enqueue\n2.dequeue\n3.display\n4.peek\n5.exit")
    opt=int(input())
    match(opt):
        case 1: enqueue()
        case 2: dequeue()
        case 3: display()
        case 4: peek()
        case 5: break







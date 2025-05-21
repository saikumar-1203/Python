class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data): 
        if self.data:  #check root is present or not
            if data<self.data:   #data less than root
                if self.left is None:   #check left node exixt or not
                    self.left=Node(data)    #if not exist create a node
                else:
                    self.left.insert(data)   #other wise insert it 
            else:                            # if data greater than root
                if self.right is None:       #check right node exixt or not
                    self.right=Node(data)    #if not exist create a node
                else:
                    self.right.insert(data)  #else insert 

def preorder(root):        #root-left-right
    if root:
        print(root.data,end=" ")          
        preorder(root.left)
        preorder(root.right)

def postorder(root):      #left-right-root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def inorder(root):         #left-root-right
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def levelorder(root):
    h=height(root)
    for p in range (1,h+1):
        current(root,p)

def current(root,level):
    if root is None:
        return 0
    else:
        if level==1:
            print(root.data,end=" ")
        else:
            current(root.left,level-1)
            current(root.right,level-1)
def zigzagorder(root):
    h=height(root)
    for p in range (1,h+1):
        currentzigzag(root,p)

def currentzigzag(root,level):
    if root is None:
        return 0
    else:
        if level==1:
            print(root.data,end=" ")
        elif level%2!=0:
            current(root.left,level-1)
            current(root.right,level-1)
        else:
            current(root.right,level-1)
            current(root.left,level-1)

def height(root):
    if root is None:
        return 0
    else:
        lh=height(root.left)
        rh=height(root.right)
    return max(lh,rh)+1

n1=Node(27)
n1.insert(14)
n1.insert(35)
n1.insert(10)
n1.insert(19)
n1.insert(31)
n1.insert(42)
print("pre order")
preorder(n1)
print("\npost order")
postorder(n1)
print("\nin order")
inorder(n1)
h=height(n1)
print("\nheight:",h)
print("\nLevele order:")
levelorder(n1)
print("\nzigzag order:")
zigzagorder(n1)



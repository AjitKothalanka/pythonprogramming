class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data
    def push(self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.push(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.push(data)
        else:
            self.data=data
    def inorder(self, root):
        res=[]
        if root:
            res=self.inorder(root.left)
            res.append(root.data)
            res=res+self.inorder(root.right)
        return res
    def preorder(self, root):
        res=[]
        if root:
            res.append(root.data)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res
    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)
        return res
x=int(input('Enter the total number of nodes including root:'))
root=Node(int(input("Enter the root node value:")))
for i in range(1,x):
    y=(int(input("Enter the node value :")))
    root.push(y)
print("----Tree Traversals---")
print("1.Inorder Traversal /n 2.Preorder Traversal /n 3.Postorder Traversal")
print("Enter any other value to Exit.")
n=int(input("Enter choice:"))
if n==1:
    print("The Inorder Traversal gives :")
    print(root.inorder(root))
elif n==2:
    print("The preorder Traversal gives :")
    print(root.preorder(root))
elif n==3:
    print("The Postorder Traversal gives :")
    print(root.postorder(root))
else :
    print("Program Terminated.")

    

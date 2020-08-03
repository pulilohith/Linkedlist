class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None 
class BST:
    def __init__(self):
        self.root=None 
    def insertion(self,root,data):
        if(not root):
            return Node(data)
        if(root.data>data):
            if(not root.left):
                root.left=Node(data)
            else:
                root.left=self.insertion(root.left,data)
        else:
            if(not root.right):
                root.right=Node(data)
            else:
                root.right=self.insertion(root.right,data) 
        return root
    def inorder(self,root):
        if(not root):
            return 
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right) 
    def searchnumber(self,root,data):
        if(not root):
            return
        if(root.data==data):
            return root
        return self.searchnumber(root.left,data) or self.searchnumber(root.right,data) 
    def deletion(self,root,data):
        if(not root):
            return 
        if(root.data<data):
            root.right=self.deletion(root.right,data)
            return root
        elif(root.data>data):
            root.left=self.deletion(root.left,data)
            return root
        else:
            if(not root.left):
                temp=root.right
                root=None 
                return temp
            elif(not root.right):
                temp=root.left
                root=None
                return temp
            else:
                parent=root
                sucessor=root.right
                while(sucessor.left):
                    parent=sucessor
                    sucessor=sucessor.left
                if(parent==root):
                    parent.right=sucessor.right
                else:
                    parent.left=sucessor.right
                root.data=sucessor.data
                return root
                
        
BS1=BST()
root=None
root=BS1.insertion(root,8)
root=BS1.insertion(root,11)
root=BS1.insertion(root,6)
root=BS1.insertion(root,9)
root=BS1.insertion(root,23) 
BS1.inorder(root) 
print(BS1.searchnumber(root,23)) 
BS1.deletion(root,8)
BS1.inorder(root)

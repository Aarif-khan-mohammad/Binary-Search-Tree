class Node():
    def __init__(self , item=None , left=None , right=None):
        self.item = item
        self.left = left
        self.right = right
    
class BST():

    def __init__(self):
        self.root = None #it holds root's instance
        
        

    def insert(self , data): #using recurssive method
        self.root = self.recursive_insert(self.root,data) # where we can pass sub tree's reffernce , which gives root node's refernce
        

    def recursive_insert(self , root , data):# here root is refers the sub tree's root node
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.recursive_insert(root.left , data)
        elif data > root.item:
            root.right = self.recursive_insert(root.right, data)
        return root
    def search(self , data):
        return self.recurive_search(self.root , data)
    
    def recurive_search(self,root , data):
        if root is None or root.item==data:
            return root
        if data<root.item:
            return self.recurive_search(root.left, data)
        else:
            return self.recurive_search(root.right, data)
        
    def inorder(self):
        result = []
        self.recurive_inorder(self.root , result)
        return result
    
    def recurive_inorder(self , root , result):
        if root:
            self.recurive_inorder(root.left, result)
            result.append(root.item)
            self.recurive_inorder(root.right, result)

    def preorder(self):
        result = []
        self.recurive_preorder(self.root , result)
        return result
    
    def recurive_preorder(self , root , result):
        if root:
            result.append(root.item)
            self.recurive_preorder(root.left, result)
            self.recurive_preorder(root.right, result)

    def postorder(self):
        result = []
        self.recurive_postorder(self.root , result)
        return result
    
    def recurive_postorder(self , root , result):
        if root:
            self.recurive_postorder(root.left, result)
            self.recurive_postorder(root.right, result)
            result.append(root.item)
    
    def min_value(self ,temp):
        current = temp
        while current.left is not None:
            current= current.left
        return current.item
    
    def max_value(self ,temp):
        current = temp
        while current.right is not None:
            current= current.right
        return current.item
    
    def delete(self , data):
        self.root = self.recursive_delete(self.root, data)


    def recursive_delete(self , root , data):
        if root is None:
            return root
        
        if data<root.item:
            root.left = self.recursive_delete(root.left , data)

        elif data>root.item:
            root.right = self.recursive_delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right) #if you want to replace current item with successor
            self.recursive_delete(root.right, root.item)
        return root
    
    def size(self):
        return len(self.inorder())

            
        
       

bst = BST()
bst.insert(20)
bst.insert(100)
bst.insert(40)
bst.insert(60)
bst.insert(80)
bst.insert(90)
bst.insert(57)
bst.insert(86)

print(bst.inorder()) #[20, 40, 57, 60, 80, 86, 90, 100]
print(bst.size())

bst.delete(57)
print(bst.inorder()) #[20, 40, 57, 60, 80, 86, 90, 100]
print(bst.size())

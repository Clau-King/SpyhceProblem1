class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            if self.value > a and self.value < b:
                print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()
                
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def inorder(self):
        self.root.inorder()
        
bst = Tree()
a = 23
b = 68
x = [50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 67]
for nod in x:
    bst.insert(nod)
bst.inorder()
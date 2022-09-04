#binary tree

class Node:
    def __init__(self,value,right = None,left= None):
        self.right = right
        self.left = left
        self.value = value

    def insert(self,value):

        if value < self.value :

            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

        else:
            self.value = value

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()
    
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printTree()

"""
    12
   6   14 
  3     
"""
        
class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insertnode(self, data):
        if self.data:
            if self.data > data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertnode(data)
            elif self.data < data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertnode(data)
            else:
                self.data = Node(data)
        
                    
    def contain(self,data):
        if(self.data > data):
            if(self.left == None):
                return False
            return self.left.contain(data)
        elif(self.data < data):
            if(self.right == None):
                return False;
            else:
                return self.right.contain(data)
        else:
            return self.data

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.data, end =" ")
        if self.right:
            self.right.printInOrder()
    
    def printPreOrder(self):
        if self.data:
            print(self.data, end =" ")
            if self.left:
                self.left.printPreOrder()
            if self.right:
                self.right.printPreOrder()


root = Node(12)
root.insertnode(6)
root.insertnode(14)
root.insertnode(3)
root.insertnode(2)

print(root.contain(3))
print(root.contain(13))

root.printInOrder()
root.printPreOrder()




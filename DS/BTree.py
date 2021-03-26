class BTree(object):

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftNode = None
        self.rightNode = None
    
    def LeftChild(self, newVal):
        if self.leftNode == None:
            self.leftNode = BTree(newVal)
        else:
            CTree = BTree(newVal)
            CTree.leftNode = self.leftNode
            self.leftNode = CTree
        #return self
    
    def RightChild(self, newVal):
        if self.rightNode == None:
            self.rightNode = BTree(newVal)
        else:
            CTree = BTree(newVal)
            CTree.rightNode = self.RightNode
            self.rightNode = CTree
        #return self

    def GetRightChild(self):
            return self.RightChild
        
    def GetLeftChild(self):
            return  self.LeftChild
        
    def getRootNode(self):
        return self.key




def inorder(tree):
    res = []
    if tree:
        res = inorder(tree.leftNode)
        res.append(tree.key)
        res =  res +  inorder(tree.rightNode)
    return res

def Preorder(tree):
    res = []
    if tree:
        res.append(tree.key)
        res = res + Preorder(tree.leftNode)
        res =  res +  Preorder(tree.rightNode)
    return res

def Postorder(tree):
    res = []
    if tree:
        res = Postorder(tree.leftNode)
        res =  res +  Postorder(tree.rightNode)
        res.append(tree.key)
    return res

r = BTree('a')
r.RightChild('R1')
r.LeftChild('L1')
r.LeftChild('L2')
IN= inorder(r)
PRE= Preorder(r)
PORT = Postorder(r)
print(IN)
print(PRE)
print(PORT)
#val= inorder(r)

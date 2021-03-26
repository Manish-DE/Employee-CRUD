class BTreeList(object):
    root = []
    def BinaryTree(r):
        return [r, [], []];

    def leftNode(root, NodeList):
        Node = root.pop(1)
        if(Node):
            root.insert(1,[NodeList,Node,[]])
        else:
            root.insert(1,[NodeList,[],[]])
        return root
    def RightNode(root, NodeList):
        Node = root.pop(2)
        if(Node):
            root.insert(2,[NodeList,[],Node])
        else:
            root.insert(2,[NodeList,[],[]])
        return root
    def getRoot(root):
        return root[0]
    
    def setRoot(root,NewVal):
        root[0]=NewVal
        
    
    def GetLNode(root):
        return root[1]
        
    def GetRNode(root):
        return root[2]
    

rootVal  = BTreeList.BinaryTree("Root")
BTreeList.leftNode(rootVal,"L1" )
BTreeList.RightNode(rootVal,"R1" )
BTreeList.RightNode(rootVal,"R2" )
BTreeList.leftNode(rootVal,"L2" )
l = BTreeList.GetLNode(rootVal)
print(l)




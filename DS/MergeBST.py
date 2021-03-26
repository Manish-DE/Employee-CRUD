class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def Insert(self, data):
        if self.data:
            if self.data > data:
                if(self.left == None):
                    self.left = Node(data)
                else:
                    self.left.Insert(data)
            elif self.data < data:
                if(self.right == None):
                    self.right = Node(data)
                else:
                    self.right.Insert(data)
            else:
                self.data = Node(data)
    def InOrder(self,arr=[]):
        if self.data:
            if self.left:
                self.left.InOrder(arr)
            arr.append(self.data)
            if self.right:
                self.right.InOrder(arr)

def InsertNode(root, data):
    if not root:
        return Node(data)
    if root.data > data:
        root.left = InsertNode(root.left, data)
    elif root.data < data:
       root.right = InsertNode(root.right, data)
    else:
        return root
    return root

def PrintInOrder(root,arr):
    if root:
        PrintInOrder(root.left, arr)
        arr.append(root.data)
        PrintInOrder(root.right, arr)

def MergerArray(arr1,arr2):
    i=j=0
    arr = []
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] <= arr2[j]):
            arr.append(arr1[i])
            i+= 1
        else:
            arr.append(arr2[j])
            j+= 1
    return arr

def ArrToBST(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = ArrToBST(arr[:mid])
    root.right = ArrToBST(arr[mid+1:])
    return root


if __name__ == '__main__':
    root1 = root2 = None
    #Insert in root1
    root1 = InsertNode(root1, 100)
    root1 = InsertNode(root1, 50)
    root1 = InsertNode(root1, 300)
    root1 = InsertNode(root1, 20)
    root1 = InsertNode(root1, 70)
 #   root1= Node(100)
 #   root1.Insert(50)
 #   root1.Insert(300)
 #   root1.Insert(20)
 #   root1.Insert(70)

    #Insert in root2
    root2 = InsertNode(root2,80)
    root2 = InsertNode(root2,40)
    root2 = InsertNode(root2,120)
 #   root2 = Node(80)
 #   root2.Insert(40)
 #   root2.Insert(120)

    arr1 = []
    PrintInOrder(root1, arr1)
#    root1.InOrder(arr1)
    arr2 = []
#    root2.InOrder(arr2)
    PrintInOrder(root2, arr2)
    arr = MergerArray(arr1,arr2)
    root = ArrToBST(arr)
    res =[]
    PrintInOrder(root, res)

    for i in res:
        print(i, end =" ")

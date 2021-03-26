class LNode:
    def __init__(self, New_Node):
        self.data = New_Node
        self.next = None

class LLNode:    
    def __init__(self):
        self.head = None

    def pushNode(self,CNode):
        NextNode = LNode(CNode)
        NextNode.next = self.head
        self.head = NextNode

    def InsertAfter(self, NewNode, PreNode):
        if PreNode is None:  
            print ("The given previous node must inLinkedList.")
            return
        NewNode = LNode(NewNode)
        NewNode.next = PreNode.next
        PreNode.next = NewNode

    def appendNode(self, NewNode):
        NewNode = LNode(NewNode)
        if self.head == None:
            self.head = NewNode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = NewNode

    def printNode(self):
        Node = self.head
        if Node.next == None:
            return
        while(Node):
            print (Node.data, end= " ")
            Node=Node.next
    
    def DeletePostion(self,position):
        Node = self.head
        if Node == None:
            return
        if position == 0:
            self.head = Node.next
            Node = None
            return
        for i in range(position -1):
            Node = Node.next
            if Node is None:
                break
        if Node.next == None:
            return
        next = Node.next.next 
        Node.next = None
        Node.next = next    

    def DeleteNode(self, Data):
        Node = self.head
        
        if Node == None:
            return

        if Node.data == Data:
            self.head = Node.next
            Node = None
            return
        
        while(Node):
            if(Node.data == Data):
                break
            Pre = Node
            Node = Node.next
        
        Pre.next =Node.next
        Node = None
    def DeleteLinkList(self):
        Node = self.head
        while Node:
            prev = Node.next
            del Node.data
            Node = prev

    # Function :- Number of Count
    def getCount(self):
        return self.getCountRec(self.head)
    def getCountRec(self, Node):
        if(not Node):
            return 0
        else:
            return 1 + self.getCountRec(Node.next)


    # Function :- To search Value
    def SearchNode(self,data):
        Node = self.head
        while Node != None:
            if Node.data == data:
                return True
            Node = Node.next
        return False

    def GetNth(self,position):
        Node = self.head

        if position == 0:
            return Node.data
        count = 0
        while Node:
            if count == position:
                return Node.data
            count = count + 1
            Node = Node.next
        return 0

        

llist = LLNode() 
llist.pushNode(9)
llist.pushNode(7) 
llist.pushNode(1) 
llist.pushNode(3) 
llist.pushNode(2) 
llist.appendNode(91)
llist.InsertAfter(20,llist.head.next) 
print("\nCreated Linked list is:") 
llist.printNode() 
print("\nCreated Linked list is:") 
llist.DeleteNode(2)
llist.printNode() 
print("\nCreated Linked list is:") 
llist.DeletePostion(4)
llist.printNode() 
#llist.DeleteLinkList()
print("\nCreated Linked list is:") 
llist.printNode() 

print("\List has Total NOde :- :", llist.getCount()) 

if llist.SearchNode(91):
    print("Yes")
else:
    print("No")

print("Nth Position Value is :- :", llist.GetNth(3)) 
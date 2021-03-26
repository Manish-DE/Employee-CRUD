class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        selft.next= next

class Solution(object):
    def removeNthFromEnd(self, head,n):
        size =1
        cur = p = head
        while (cur.next != Null):
            size += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
            if size == n:
                return head.next
            else:
                p.next = p.next.next
                return head


mylist = Solution()
head = [1,2,3,4,5], 
mylist.removeNthFromEnd(head,2)
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        if head == None:
            return None
            
        dummyHead = ListNode(None)
        dummyHead.next = head
        cur = head
        
        while cur.next:
            if  cur.next.val < cur.val:
                pre = dummyHead
                while pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
                
            else:
                cur =cur.next
        return dummyHead.next
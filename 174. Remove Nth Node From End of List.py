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
    @param: n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # res = tmp =ListNode(0)
        # tmp.next = head
        # p = tmp
        # q = tmp
        # for i in range(n + 1):
        #     q = q.next
        
        # while q:
        #     p = p.next
        #     q = q.next
            
        # p.next = p.next.next
        
        # return res.next
        dummyHead = ListNode(None)
        dummyHead.next = head
        
        p = dummyHead
        q = dummyHead
        
        for i in range(0, n + 1):
            q = q.next
            
        while q:
            p = p.next
            q = q.next
            
        p.next = p.next.next
        return dummyHead.next
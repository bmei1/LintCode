"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        if head == None:
            return None
        ahead = ListNode(None)
        bhead = ListNode(None)
        alist = ahead
        blist = bhead
        cur = head
        while cur:
            if cur.val < x:
                alist.next = cur
                alist = alist.next
                
            else:
                blist.next = cur
                blist = blist.next
            cur = cur.next
        
        alist.next = bhead.next
        blist.next = None
        
        return ahead.next
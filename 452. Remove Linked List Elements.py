"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        if head == None:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head
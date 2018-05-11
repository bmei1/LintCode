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
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        if head == None:
            return None
        left = head
        right = head
        for i in range(n - 1):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        return left
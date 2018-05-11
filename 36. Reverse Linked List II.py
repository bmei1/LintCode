"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: ListNode head is the head of the linked list 
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        i = 0
        tmp = ListNode(None)
        tmp.next = head
        pre = tmp
        while i < m - 1:
            pre = pre.next
            i += 1
        cur = pre.next
        j = 0
        while j < n - m:
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
            j += 1
        return tmp.next
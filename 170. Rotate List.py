"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution:
    """
    @param: head: the List
    @param: k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if head == None:
            return None
        if k == 0:
            return head

        dummyHead = ListNode(None)
        dummyHead.next = head
        tmp1 = tmp2 = ListNode(None)
        tmp1.next = tmp2.next = dummyHead
        
        p = dummyHead
        q = dummyHead
        
        count = 0
        while p.next:
            p = p.next
            count += 1

        p = dummyHead
        k = k % count
        if k == 0:
            return head
        
        for i in range(0, k):
            q = q.next
            tmp1 = tmp1.next
            
        while q:
            q = q.next
            p = p.next
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        
        dummyHead.next = p
        tmp2.next = None
        tmp1.next = head
        
        return dummyHead.next
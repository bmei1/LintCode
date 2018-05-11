"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        # res = tmp = ListNode(0)
        # tmp.next = head
        # while tmp.next and tmp.next.next:
        #     n1 = tmp.next
        #     n2 = n1.next
        #     n3 = n2.next
            
        #     n2.next = n1
        #     n1.next = n3
        #     tmp.next = n2
        #     tmp = n1
        # return res.next
        dummyHead = ListNode(None)
        dummyHead.next = head
        pre = dummyHead
        
        while pre.next and pre.next.next:
            node1 = pre.next
            node2 = node1.next
            next = node2.next
            
            node2.next = node1
            node1.next = next
            pre.next = node2
            
            pre = node1
        
        return dummyHead.next
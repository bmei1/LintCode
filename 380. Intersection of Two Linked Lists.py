"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        if  not headA or not headB:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            if pA == None:
                pA = headB
            else:
                pA = pA.next
            if pB == None:
                pB = headA
            else:
                pB = pB.next
        return pA
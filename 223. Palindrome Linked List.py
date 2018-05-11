"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        for i in range(len(temp) // 2):
            if temp[i] != temp[len(temp) - 1 - i]:
                return False
        return True
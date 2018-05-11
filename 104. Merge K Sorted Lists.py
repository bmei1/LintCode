"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        import heapq
        dummyHead = ListNode(None)
        head = dummyHead
        
        pq = []
        for i in lists:
            if i:
                heapq.heappush(pq, (i.val, i))
        
        while pq:
            val, node = heapq.heappop(pq)
            dummyHead.next = node
            dummyHead = dummyHead.next
            node = node.next
            if node:
                heapq.heappush(pq, (node.val, node))
        return head.next
        
        # from Queue import PriorityQueue
        # head = point = ListNode(0)
        # q = PriorityQueue()
        # for l in lists:
        #     if l:
        #         q.put((l.val, l))
        # while not q.empty():
        #     val, node = q.get()
        #     point.next = node
        #     point = point.next
        #     node = node.next
        #     if node:
        #         q.put((node.val, node))
        # return head.next
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        pq = []
        res = []
        for key in freq:
            heapq.heappush(pq, (-freq[key], key))
            
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
            
        return res
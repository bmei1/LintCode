class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        for k in C:
            for l in D:
                if k + l in dic:
                    dic[k + l] += 1
                else:
                    dic[k + l] = 1
        
        res = 0
        for i in A:
            for j in B:
                if 0 - i - j in dic:
                    res += dic[0 - i - j]
        return res
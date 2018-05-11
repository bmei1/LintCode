class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        dic = {}
        for i in range(len(A)):
            if A[i] in dic:
                dic[A[i]] += 1
            else:
                dic[A[i]] = 1
        for j in dic:
            if dic[j] == 1:
                return j
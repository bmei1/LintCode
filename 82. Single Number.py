class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i
        return result
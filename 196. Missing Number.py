class Solution:
    """
    @param: nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                res = i
        return res
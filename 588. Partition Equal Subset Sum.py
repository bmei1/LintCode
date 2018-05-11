class Solution:
    """
    @param: nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        c = s // 2
        memo = [False] * (c + 1)
        for i in range(0, c + 1):
            memo[i] = (nums[0] == i)
        for i in range(1, n):
            for j in range(c, nums[i] - 1, -1):
                memo[j] = memo[j] or memo[j - nums[i]]
        return memo[c]
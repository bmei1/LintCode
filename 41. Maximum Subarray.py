class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        max_curt = max_gobal = nums[0]
        for i in xrange(1, len(nums)):
            max_curt = max(nums[i], max_curt + nums[i])
            if max_curt > max_gobal:
                max_gobal = max_curt
        return max_gobal
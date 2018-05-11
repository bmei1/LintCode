class Solution:
    """
    @param: nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        product = nums[0]
        curmax = nums[0]
        curmin = nums[0]
        for i in range(1, len(nums)):
            maxnext = curmax * nums[i]
            minnext = curmin * nums[i]
            curmax = max(nums[i], max(maxnext, minnext))
            curmin = min(nums[i], min(maxnext, minnext))
            product = max(product, curmax)
        return product
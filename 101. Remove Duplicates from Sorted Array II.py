class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        i = 0
        for j in nums:
            if i < 2 or j > nums[i - 2]:
                nums[i] = j
                i += 1
        return i
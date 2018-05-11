class Solution:
    """
    @param: nums: an integer array
    @return: 
    """
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(0)
        return nums
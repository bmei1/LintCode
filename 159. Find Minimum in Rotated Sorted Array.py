class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if len(nums) == 0:
            return
        left = 0
        right = len(nums) - 1
        while left < right and nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
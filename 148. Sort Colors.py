class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        zero = -1
        two = len(nums)
        i = 0
        while i < two:
            if nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            if nums[i] == 0:
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
            if nums[i] == 1:
                i += 1
        return nums
class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        l = 0
        r = -1
        sum = 0
        ans = len(nums) + 1
        while l < len(nums):
            if sum < s and r + 1 < len(nums):
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1
                
            if sum >= s:
                ans = min(ans, r - l + 1)
                
        if ans == len(nums) + 1:
            return -1

        return ans
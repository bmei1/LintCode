class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        if nums == None:
            return None
        a = {}
        for b in nums:
            if b not in a:
                a[b] = 1
            else:
                a[b] += 1
        i = sorted(a, key=lambda x:a[x])[-1]
        if a[i] >= len(nums)//2 + 1:
            return i
        else:
            return None
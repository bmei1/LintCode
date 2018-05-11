class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        res = []
        used = [False] * len(nums)
        p = []
        self.generatePerm(nums, 0, p, res, used)
        return res
        
    def generatePerm(self, nums, index, p, res, used):
        if index == len(nums):
            res.append(p[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                p.append(nums[i])
                used[i] = True
                self.generatePerm(nums, index + 1, p, res, used)
                p.pop()
                used[i] = False
        return
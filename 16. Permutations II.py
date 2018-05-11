class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        res = []
        used = [False] * len(nums)
        p = []
        self.generatePerm(nums, 0, p, res, used)
        # res_set = set(map(tuple,res)) 
        # res = map(list,res_set)
        res_new = []
        for i in res:
            if i not in res_new:
                res_new.append(i)
        return res_new
        
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
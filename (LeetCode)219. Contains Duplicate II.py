class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = set()
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            record.add(nums[i])
            
            if len(record) == k+1:
                record.remove(nums[i - k])
        return False
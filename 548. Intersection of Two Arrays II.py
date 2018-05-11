class Solution:
    
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        a = {}
        for i in range(len(nums1)):
            if nums1[i] in a:
                a[nums1[i]] += 1
            else:
                a[nums1[i]] = 1
        
        b = []
        for j in range(len(nums2)):
            if a.get(nums2[j]) > 0:
                b.append(nums2[j])
                a[nums2[j]] -= 1
        
        return b
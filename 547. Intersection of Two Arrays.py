class Solution:
    
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        a = set()
        for i in range(len(nums1)):
            a.add(nums1[i])
            
        b = set()
        for j in range(len(nums2)):
            if nums2[j] in a:
                b.add(nums2[j])
        
        return list(b)
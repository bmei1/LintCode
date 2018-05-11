class Solution:
    """
    @param: heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > res:
                res = area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
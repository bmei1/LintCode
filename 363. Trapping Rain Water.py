class Solution:
    """
    @param: heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        if len(heights) < 3:
            return 0
        sum = 0
        leftmax = 0
        rightmax = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            leftmax = max(leftmax, heights[l])
            rightmax = max(rightmax, heights[r])
            if leftmax < rightmax:
                sum += leftmax - heights[l]
                l += 1
            else:
                sum += rightmax - heights[r]
                r -= 1
        return sum
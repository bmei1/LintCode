class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        a = [0, 1, 2]
        for i in range(3, n+1):
            a.append(a[i-2] + a[i-1])
        return a[n]
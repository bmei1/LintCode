class Solution:
    """
    @param: A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[n - 1]
        if n == 2:
            return max(A[n - 2], A[n - 1])
        memo = [-1] * n
        memo[n - 1] = A[n - 1]
        memo[n - 2] = A[n - 2]
        memo[n - 3] = A[n - 3] + memo[n - 1]
        for i in range(n - 4, -1, -1):
            memo[i] = A[i] + max(memo[i + 2], memo[i + 3])
        return max(memo[0], memo[1])
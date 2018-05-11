class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        a = len(A)
        b = len(B)
        memo = [[0] * (b + 1) for i in range(a + 1)]
                
        for i in range(a):
            for j in range (b):
                if A[i] == B[j]:
                    memo[i + 1][j + 1] = 1 + memo[i][j]
                else:
                    memo[i + 1][j + 1] = max(memo[i][j + 1], memo[i + 1][j])
        return memo[a][b]
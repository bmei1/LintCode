class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        #write your code here
        # dp = [False for i in range(len(s)+1)]
        # dp[0] = True
        # for i in range(1, len(s)+1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in dict:
        #             dp[i] = True
        # return dp[len(s)]
        
        
        if len(dict) == 0:
            return len(s) == 0
            
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        
        maxLength = max([len(w) for w in dict])
        for i in xrange(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):
                if not f[i - j]:
                     continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break
        
        return f[n]
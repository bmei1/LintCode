class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        ans = ""
        for i in range(len(s)):
            temp = self.judge(s, i, i)
            if len(ans) < len(temp):
                ans = temp
            temp = self.judge(s, i, i+1)
            if len(ans) < len(temp):
                ans = temp
        return ans
        
    def judge(self, s, a, b):
        while a >= 0 and b < len(s) and s[a] == s[b]:
            a -= 1; b += 1
        return s[a+1:b]
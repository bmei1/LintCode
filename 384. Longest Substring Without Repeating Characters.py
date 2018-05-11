class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        # ans = 0
        # j = 0   #left margin
        # k = {}  #record letter
        # for i in range(len(s)):
        #     if s[i] in k and k[s[i]] >= j:
        #         j = k[s[i]] + 1 #move left
        #     k[s[i]] = i
        #     ans = max(ans, i-j+1)
        # return ans
        
        l = 0
        r = -1
        ans = 0
        freq = [0] * 256
        while l < len(s):
            if r + 1 < len(s) and freq[ord(s[r + 1])] == 0:
                r += 1
                freq[ord(s[r])] += 1
            else:
                freq[ord(s[l])] -= 1
                l += 1
        
            ans = max(ans, r - l + 1)
        
        return ans
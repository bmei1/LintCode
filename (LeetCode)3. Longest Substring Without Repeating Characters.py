class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = -1
        ans = 0
        freq = [0 for x in range(256)]
        while l < len(s):
            if r + 1 < len(s) and freq[ord(s[r + 1])] == 0:
                r += 1
                freq[ord(s[r])] += 1
            else:
                freq[ord(s[l])] -= 1
                l += 1
        
            ans = max(ans, r - l + 1)
        
        return ans
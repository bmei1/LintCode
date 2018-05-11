class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        r = 0
        res = []
        count = len(p)
        freq = [0] * 256
        for i in p:
            freq[ord(i)] += 1
        while r < len(s):
            if freq[ord(s[r])] > 0: 
                count -= 1
            freq[ord(s[r])] -= 1
            if r >= len(p):
                if freq[ord(s[r - len(p)])] >= 0:
                    count += 1
                freq[ord(s[r - len(p)])] += 1
            if count == 0:
                res.append(r - len(p) + 1)
            r += 1
        return res
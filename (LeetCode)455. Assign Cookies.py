class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        list.sort(g)
        list.sort(s)
        
        i = len(g) - 1
        j = len(s) - 1
        res = 0
        
        while  i >= 0 and j >= 0:
            if s[j] >= g[i]:
                i -= 1
                j -= 1
                res += 1
            else:
                i -= 1
                
        return res
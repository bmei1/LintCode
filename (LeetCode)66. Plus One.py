class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = ''
        i = 0
        ans =[]
        while i < len(digits):
            a += str(digits[i]) 
            i += 1
        b = str(int(a) + 1)
        c = [i for i in b]
        for d in c:
            ans.append(int(d))
        return ans
class Solution:
    # @param {string} s Roman representation
    # @return {int} an integer
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for i in range(len(s)-1):
            curt = d[s[i]] 
            next = d[s[i+1]]
            if curt >= next:
                num += curt
            else:
                num -= curt
        num += d[s[len(s)-1]]
        return num
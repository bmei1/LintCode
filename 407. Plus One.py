class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits): 
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
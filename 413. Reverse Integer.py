class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        if n < 0:
            a = int("-" + str(-n)[::-1])
            if a < -2**31:
                return 0
            else: 
                return a
        else:
            b = int(str(n)[::-1])
            if b > 2**31-1:
                return 0
            else:
                return b
                
        #32bit range (-2**31, 2**31-1)
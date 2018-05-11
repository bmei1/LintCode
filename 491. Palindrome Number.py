class Solution:
    # @param {int} num a positive number
    # @return {boolean} true if it's a palindrome or false
    def palindromeNumber(self, num):
        if len(str(num)) % 2 == 0:
            if str(num)[:len(str(num))//2] == str(num)[:len(str(num))//2-1:-1]:
                return True
            else:
                return False
        else:
            if str(num)[:len(str(num))//2] == str(num)[:len(str(num))//2:-1]:
                return True
            else:
                return False
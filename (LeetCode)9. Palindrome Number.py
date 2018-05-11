class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if len(str(x)) % 2 == 0:
            if str(x)[:len(str(x))//2] == str(x)[:len(str(x))//2-1:-1]:
                return True
            else:
                return False
        else:
            if str(x)[:len(str(x))//2] == str(x)[:len(str(x))//2:-1]:
                return True
            else:
                return False
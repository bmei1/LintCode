class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        pow = 1
        if n == 0:
            return pow
        if n < 0:
            x = 1/x
            n = -n
        while n:
            if n & 0x01 == 1:
                pow *= x
            x *= x
            n >>= 1  # n divided by 2
        return pow
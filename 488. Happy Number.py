class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        nums = set()
        while True:
            nums.add(n)
            sum = 0
            # while n > 0:
            #     sum += (n % 10) ** 2
            #     n /= 10
            for i in str(n):
                sum += int(i) ** 2
            if sum == 1:
                return True
            if sum in nums:
                return False
            else:
                n = sum
class Solution:
    """
    @param: n: Given the range of numbers
    @param: k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):       
        res = []
        if n <= 0 or k <= 0 or n < k:
            return res
        c = []
        
        def generateComb(n, k, start, c):
            if len(c) == k:
                res.append(c[:])
                return
            
            for i in range(start, n - (k - len(c)) + 2):
                c.append(i)
                generateComb(n, k, i + 1, c)
                c.pop()
            return
        
        generateComb(n, k, 1, c)
        return res
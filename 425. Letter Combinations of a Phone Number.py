class Solution:
    """
    @param: digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        res = []
        ch = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for i in digits:
            tmp = []
            for j in ch[int(i)]:
                if len(res) == 0:
                    tmp.append(j)
                else:
                    for k in res:
                        tmp.append(k + j)
            res = tmp
        return res
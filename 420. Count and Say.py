class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def count(self, s):
        t = ''
        count = 0
        curr = '_'
        for i in s:
            if i != curr:
                if curr != '_':
                    t += str(count) + curr
                curr = i
                count = 1
            else:
                count += 1
        t += str(count) + curr
        return t

    def countAndSay(self, n):
        s = '1'
        for i in range(1, n):
            s = self.count(s)
        return s
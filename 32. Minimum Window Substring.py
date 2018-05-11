class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        count = len(target)
        freq = [0] * 256
        for i in target:
            freq[ord(i)] += 1
        l = 0
        r = 0
        minlen = len(source) + 1
        while r < len(source):
            if freq[ord(source[r])] >0:
                count -= 1   
            freq[ord(source[r])] -= 1
            r += 1
            while count == 0:
                if r - l < minlen:
                    minl = l
                    minlen = r - l
                freq[ord(source[l])] += 1
                if freq[ord(source[l])] > 0:
                    count += 1
                l += 1
        if minlen > len(source): 
            return ""
        return source[minl: minl + minlen]
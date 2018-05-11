class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            freq = [0] * 256
            for i in range(len(s)):
                freq[ord(s[i])] += 1
                freq[ord(t[i])] -= 1
            if freq == [0] * 256:
                return True
            else:
                return False
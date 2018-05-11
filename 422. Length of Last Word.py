class Solution:
    """
    @param: s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        if s == "":
            return 0
        if s[len(s) - 1] == " ":
            s = s[:len(s) - 1]
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                return len(s[i + 1:])
        return len(s)
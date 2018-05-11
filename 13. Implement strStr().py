class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if target == "":
            return 0
        if not source or not target:
            return -1
        for i in range(len(source)):
            if source[i:i+len(target)] == target:
                return i
        return -1
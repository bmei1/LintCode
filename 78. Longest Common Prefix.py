class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        if strs == [] or '' in strs:
            return ''
        for i in range(len(strs[0])):
            for j in strs:
                if len(j) <= i or j[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
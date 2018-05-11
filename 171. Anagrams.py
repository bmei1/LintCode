class Solution:
    """
    @param: strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        res = []
        dic = {}
        for i in strs:
            sword = "".join(sorted(i))
            if sword not in dic.keys():
                dic[sword] = [i]
            else:
                dic[sword] = dic[sword] + [i]
        for j in dic:
            if len(dic[j]) >= 2:
                res += dic[j]
        return res
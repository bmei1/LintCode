class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dic = {}
        tmp = strs[:]
        for i in range(len(tmp)):
            tmp[i] = "".join(sorted(tmp[i]))
        
        for j in range(len(tmp)):
            if tmp[j] in dic:
                dic[tmp[j]].append(strs[j])
            else:
                dic[tmp[j]] = [strs[j]]
                
        for k in dic:
            res.append(dic[k])
            
        return res
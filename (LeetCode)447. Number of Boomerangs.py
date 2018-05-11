class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        
        for i in points:
            dic = {}
            for j in points:
                if i != j:
                    if dis(i, j) in dic:
                        dic[dis(i, j)] += 1
                    else:
                        dic[dis(i, j)] = 1
                        
            for k in dic.keys():
                res += dic[k] * (dic[k] - 1)
            
        return res
                        
def dis(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
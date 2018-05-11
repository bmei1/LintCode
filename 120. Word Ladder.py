class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # d = {}
        # for word in dict:
        #     for i in range(len(word)):
        #         tmp = [:i] + "_" + [i+1:]
        #         if tmp in d:
        #             d[tmp].append(word)
        #         else:
        #             d[tmp] = [word]
        dict.add(end)
        tmp = [(start, 1)]
        while tmp:
            cur, count = tmp.pop(0)
            if cur == end:
                return count
            for i in range(len(start)):
                l = cur[:i]
                r = cur[i+1:]
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    if cur[i] != c:
                        changedword = l + c + r
                        if changedword in dict:
                            tmp.append((changedword, count + 1))
                            dict.remove(changedword)
        return 0
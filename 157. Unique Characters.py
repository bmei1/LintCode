class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        tmp = ""
        for i in str:
            if i not in tmp:
                tmp += i 
            else:
                return False
        return True
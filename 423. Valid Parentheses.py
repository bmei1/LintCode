class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if stack == []:
                    return False
                j = stack.pop()
                if i == ')' and j != '(':
                    return False
                if i == ']' and j != '[':
                    return False
                if i == '}' and j != '{':
                    return False
        return stack == []

        # temp = [None]
        # map = {')':'(', ']':'[', '}':'{'}
        # if len(s)%2 != 0:
        #     return False
        # for i in s:
        #     if i in map and map[i] == temp[len(temp) - 1]:
        #         temp.pop()
        #     else:
        #         temp.append(i)
        # return len(temp) == 1
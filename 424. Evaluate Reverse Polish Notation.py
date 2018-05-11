class Solution:
    """
    @param: tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    stack.append(num1 + num2)
                if i == "-":
                    stack.append(num1 - num2)
                if i == "*":
                    stack.append(num1 * num2)
                if i == "/":
                    stack.append(int(num1 * 1.0 / num2))
        return stack.pop()
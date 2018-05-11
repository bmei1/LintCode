"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        # def dfs(root, val):
        #     if not root.left and not root.right:
        #         res.append(val)
        #     if root.left:
        #         dfs(root.left, val + '->' + str(root.left.val))
        #     if root.right:
        #         dfs(root.right, val + '->' + str(root.right.val))
        
        # res = []
        # if not root:
        #     return res
        # dfs(root, str(root.val))    
        # return res
        
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            res.append(str(root.val))
            return res
        leftS = self.binaryTreePaths(root.left)
        for i in range(len(leftS)):
            res.append(str(root.val) + '->' + leftS[i])
        rightS = self.binaryTreePaths(root.right)
        for i in range(len(rightS)):
            res.append(str(root.val) + '->' + rightS[i])
        return res
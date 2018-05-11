"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        def dfs(root, val, val_list):
            if not root.left and not root.right:
                if val == target:
                    return ans.append(val_list)
            if root.left:
                dfs(root.left, val + root.left.val, val_list + [root.left.val])
            if root.right:
                dfs(root.right, val + root.right.val, val_list + [root.right.val])
        
        ans = []
        if not root:
            return ans
        dfs(root, root.val, [root.val])
        return ans
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if not root:
            return[]
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
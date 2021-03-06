"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        if root in (None, A, B):
            return root
        l = self.lowestCommonAncestor(root.left, A, B)
        r = self.lowestCommonAncestor(root.right, A, B)
        if l and r:
            return root
        return l or r
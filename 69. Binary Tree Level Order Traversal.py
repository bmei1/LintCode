"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        # if not root:
        #     return []
        # q = [[root]]
        # for level in q:
        #     r = []
        #     for node in level:
        #         if node.left:
        #             r.append(node.left)
        #         if node.right:
        #             r.append(node.right)
        #     if r:
        #         q.append(r)
                
        # return [[x.val for x in level] for level in q]
        
        res = []
        self.preorder(root, 0, res)
        return res
        
    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)
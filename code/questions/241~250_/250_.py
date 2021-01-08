"""
https://leetcode-cn.com/problems/count-univalue-subtrees/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left is root.right is None:
            return 1
        left = self.countUnivalSubtrees(root.left)
        right = self.countUnivalSubtrees(root.right)
        is_same = True
        if left and root.left.val != root.val:
            is_same = False
        if right and root.right.val != root.val:
            is_same = False
        return left + right + 1 if is_same else left + right

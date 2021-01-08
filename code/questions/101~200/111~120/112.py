"""
https://leetcode-cn.com/problems/path-sum
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        elif root.left is root.right is None:
            return sum == root.val
        else:
            return self.hasPathSum(root.right, sum-root.val) or self.hasPathSum(root.left, sum-root.val)

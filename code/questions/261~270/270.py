"""
https://leetcode-cn.com/problems/closest-binary-search-tree-value/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return float('inf')
        if target < root.val:
            left = self.closestValue(root.left, target)
            return left if abs(left-target) < abs(root.val-target) else root.val
        else:
            right = self.closestValue(root.right, target)
            return right if abs(right-target) < abs(root.val-target) else root.val

"""
https://leetcode-cn.com/problems/balanced-binary-tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.get_height(root.left) - self.get_height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(
            self.get_height(root.left),
            self.get_height(root.right),
        )

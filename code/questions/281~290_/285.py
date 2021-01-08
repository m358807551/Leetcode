"""
https://leetcode-cn.com/problems/inorder-successor-in-bst/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        rst = None
        while root:
            if p.val < root.val:
                rst = root
                root = root.left
            else:
                root = root.right
        return rst

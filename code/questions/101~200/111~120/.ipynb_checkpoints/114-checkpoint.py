"""
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def flatten(self, root):
        if not root:
            return None
        elif root.left is root.right is None:
            return root
        elif not root.right:
            root.right = root.left
            root.left = None
            return self.flatten(root.right)
        elif not root.left:
            return self.flatten(root.right)
        else:
            rst = self.flatten(root.right)
            self.flatten(root.left).right = root.right
            root.right = root.left
            root.left = None
            return rst

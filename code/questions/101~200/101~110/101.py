"""
https://leetcode-cn.com/problems/symmetric-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.res(root.left, root.right)

    def res(self, p, q):
        if (p and q) is None:
            return p is q

        if p.val != q.val:
            return False

        return self.res(p.left, q.right) and self.res(p.right, q.left)

"""
https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inorder(root)[k-1]

    def inorder(self, r):
        return self.inorder(r.left) + [r.val] + self.inorder(r.right) if r else []

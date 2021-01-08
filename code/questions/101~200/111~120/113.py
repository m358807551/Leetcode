"""
https://leetcode-cn.com/problems/path-sum-ii
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        self.rst = []
        self.backtrace([], root, sum)
        return self.rst

    def backtrace(self, trace, root, sum):
        if not root:
            return
        if root.left is root.right is None:
            if sum == root.val:
                self.rst.append(trace+[root.val])
            return
        trace.append(root.val)
        self.backtrace(trace, root.left, sum-root.val)
        trace.pop(-1)

        trace.append(root.val)
        self.backtrace(trace, root.right, sum - root.val)
        trace.pop(-1)

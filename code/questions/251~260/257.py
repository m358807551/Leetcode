"""
https://leetcode-cn.com/problems/binary-tree-paths/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.rst = []
        self.backtrace([], root)
        return self.rst

    def backtrace(self, trace, node):
        if not node:
            return
        if node.left is node.right is None:
            self.rst.append('->'.join(trace + [str(node.val)]))
            return

        trace.append(str(node.val))
        if node.left:
            self.backtrace(trace, node.left)
        trace.pop(-1)

        trace.append(str(node.val))
        if node.right:
            self.backtrace(trace, node.right)
        trace.pop(-1)

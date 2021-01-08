"""
https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        bak = [1]
        if root.right and (root.right.val == root.val + 1):
            bak.append(1 + self.longestConsecutive(root.right))
        else:
            bak.append(self.longestConsecutive(root.right))

        if root.left and (root.left.val == root.val + 1):
            bak.append(1 + self.longestConsecutive(root.left))
        else:
            bak.append(self.longestConsecutive(root.left))

        return max(bak)

"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        reverse = False
        rst = []
        queue = [[root]]
        while queue:
            line = [node.val for nodes in queue for node in nodes if node]
            if reverse:
                line = line[::-1]
            reverse = not reverse
            if line:
                rst.append(line)
            queue = [[node.left, node.right] for nodes in queue for node in nodes if node]
        return rst


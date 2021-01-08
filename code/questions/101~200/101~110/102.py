"""
https://leetcode-cn.com/problems/binary-tree-level-order-traversal
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        queue = [[root]]
        while queue:
            line = [node.val for nodes in queue for node in nodes if node]
            if line:
                rst.append(line)
            queue = [(node.left, node.right) for nodes in queue for node in nodes if node]
        return rst

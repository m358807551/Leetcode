"""
https://leetcode-cn.com/problems/binary-tree-preorder-traversal
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        rst = []
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            if isinstance(cur, TreeNode):
                stack.extend([cur.right, cur.left, cur.val])
            elif isinstance(cur, int):
                rst.append(cur)
        return rst

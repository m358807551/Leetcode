"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        stack = [root]
        while stack:
            x = stack.pop(-1)
            if x is None:
                continue
            elif isinstance(x, TreeNode):
                stack.extend([x.right, x.val, x.left])
            else:
                rst.append(x)
        return rst

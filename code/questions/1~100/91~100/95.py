"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii
"""

# Definition for a binary tree node.
from copy import deepcopy


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.res(1, n)

    def res(self, left, right):
        if left > right:
            return [None]
        if left == right:
            return [TreeNode(left)]

        rst = []
        for i in range(left, right+1):
            left_trees = self.res(left, i-1)
            right_trees = self.res(i+1, right)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    rst.append(TreeNode(i, left_tree, right_tree))
        return rst



a = Solution().generateTrees(3)
print(a)

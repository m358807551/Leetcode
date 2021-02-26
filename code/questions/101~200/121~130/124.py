"""
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
"""
from code.leetcode import make_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rst = float('-inf')
        self.res(root)
        return self.rst

    def res(self, root):
        if not root:
            return 0
        left = self.res(root.left)
        right = self.res(root.right)

        self.rst = max(self.rst, root.val + max(left, 0) + max(right, 0))

        return max(
            root.val,
            root.val + left,
            root.val + right,
        )


def main():
    """测试入口."""
    root = make_tree('[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]')
    print(Solution().maxPathSum(root))


if __name__ == '__main__':
    main()

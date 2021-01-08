"""
https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rst = 0
        self.backtrace(0, root)
        return self.rst

    def backtrace(self, trace, root):
        if not root:
            return
        if root.left is root.right is None:
            self.rst += trace * 10 + root.val
            return
        self.backtrace(trace * 10 + root.val, root.left)
        self.backtrace(trace * 10 + root.val, root.right)




def main():
    nodes = [TreeNode(i) for i in range(4)]
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]

    print(
        Solution().sumNumbers(nodes[1])
    )


if __name__ == '__main__':
    main()

"""
https://leetcode-cn.com/problems/binary-search-tree-iterator
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = [root]

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while self.stack:
            top = self.stack.pop(-1)
            if top is None:
                continue
            if isinstance(top, int):
                return top
            else:
                self.stack.extend([top.right, top.val, top.left])

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        while self.stack and self.stack[-1] is None:
            self.stack.pop(-1)
        return True if self.stack else False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

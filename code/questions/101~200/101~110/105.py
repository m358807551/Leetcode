"""
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        i = 0
        while inorder[i] != preorder[0]:
            i += 1
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root


def main():
    a = [3, 9, 20, 15, 7]
    b = [9, 3, 15, 20, 7]
    print(Solution().buildTree(a, b))


if __name__ == '__main__':
    main()

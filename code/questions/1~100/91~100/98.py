"""
https://leetcode-cn.com/problems/validate-binary-search-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        stack = [root]
        last = None
        while stack:
            x = stack.pop(-1)
            if isinstance(x, TreeNode):
                stack.extend([x.right, x.val, x.left])
            elif x is None:
                continue
            else:
                if last is not None and (x <= last):
                    return False
                last = x
        return True


def main():
    node6 = TreeNode(6)
    node20 = TreeNode(20)
    node15 = TreeNode(15, node6, node20)
    node5 = TreeNode(5)
    node10 = TreeNode(10, node5, node15)
    print(Solution().isValidBST(node10))


if __name__ == '__main__':
    main()

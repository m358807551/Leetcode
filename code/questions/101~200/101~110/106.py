"""
https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        i = 0
        while postorder[-1] != inorder[i]:
            i += 1
        root =  TreeNode(postorder[-1])
        root.left = self.buildTree(inorder[: i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root


def main():
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    print(
        Solution().buildTree(inorder, postorder)
    )

if __name__ == '__main__':
    main()

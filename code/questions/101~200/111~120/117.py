"""
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
"""
from leetcode.utils import make_tree


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return '{}'.format(self.val)


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root or (root.left is root.right is None):
            return root
        x = root.next
        while x:
            if x.left or x.right:
                break
            x = x.next

        if root.right and x:
            root.right.next = x.left or x.right
        if root.left:
            if x:
                root.left.next = root.right or x.left or x.right
            else:
                root.left.next = root.right

        self.connect(root.right)
        self.connect(root.left)
        return root


def main():
    root = make_tree('[1, 2, 3, 4, 5, 6, 7, 8, null, 9, 10, null, null, 11, 12, null, null, null, null, 13]')
    rst = Solution().connect(root)
    print(rst)


if __name__ == '__main__':
    main()

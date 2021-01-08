"""
https://leetcode-cn.com/problems/recover-binary-search-tree
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        last = p1 = p2 = None
        while cur:
            if cur.left:
                most_right = cur.left
                while most_right.right and (most_right.right is not cur):
                    most_right = most_right.right
                if most_right.right:
                    if last.val >= cur.val:
                        if p1:
                            p2 = cur
                        else:
                            p1, p2 = last, cur
                    last = cur
                    most_right.right = None
                    cur = cur.right
                else:
                    most_right.right = cur
                    cur = cur.left
            else:
                if last and last.val >= cur.val:
                    if p1:
                        p2 = cur
                    else:
                        p1, p2 = last, cur
                last = cur
                cur = cur.right
        p1.val, p2.val = p2.val, p1.val


def main():
    # nodes = [TreeNode(i) for i in range(11)]
    # nodes[6].left = nodes[4]
    # nodes[6].right = nodes[9]
    # nodes[4].left = nodes[2]
    # nodes[4].right = nodes[5]
    # nodes[2].left = nodes[1]
    # nodes[2].right = nodes[3]
    # nodes[9].left = nodes[7]
    # nodes[9].right = nodes[10]
    # nodes[7].right = nodes[8]

    nodes = [TreeNode(i) for i in range(4)]
    nodes[1].left = nodes[3]
    nodes[3].right = nodes[2]

    rst = Solution().recoverTree(nodes[1])
    print(rst)


if __name__ == '__main__':
    main()

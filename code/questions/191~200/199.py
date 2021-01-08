"""
https://leetcode-cn.com/problems/binary-tree-right-side-view/submissions/
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        queue = [(root,)]
        while queue:
            rst.extend([
                node.val
                for nodes in queue
                for node in nodes
                if node
            ][-1:])
            queue = [
                (node.left, node.right)
                for nodes in queue
                for node in nodes
                if node
            ]

        return rst


def main():
    nodes = [TreeNode(i) for i in range(6)]
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[2].right = nodes[5]
    nodes[3].right = nodes[4]

    print(
        Solution().rightSideView(
            nodes[1]
        )
    )


if __name__ == '__main__':
    main()

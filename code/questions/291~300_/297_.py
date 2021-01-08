"""
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
todo: 层序化遍历不会
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from functools import reduce


class Codec:

    def serialize(self, root):
        s = ""
        queue = [root]
        while queue:
            root = queue.pop(0)
            if root:
                s += str(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                s += "n"
            s += " "
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = [None]
        for x in data.split(','):
            if x == 'inf':
                arr.append(None)
            else:
                arr.append(TreeNode(int(x)))

        for i in range(1, len(arr)):
            if not arr[i]:
                continue
            arr[i].left = arr[i*2] if i*2 < len(arr) else None
            arr[i].right = arr[i*2+1] if i*2+1 < len(arr) else None

        return arr[1]

def main():
    nodes = [TreeNode(i) for i in [0, 1, 2, 3, 4, 5, 6, 7]]
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[3].left = nodes[4]
    nodes[3].right = nodes[5]
    nodes[4].left = nodes[6]
    nodes[4].right = nodes[7]

    c = Codec()
    r = c.deserialize(c.serialize(nodes[1]))
    print(1)

main()
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

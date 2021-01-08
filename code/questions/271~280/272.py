"""
https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii/

# todo: 节点遍历前一节点和后一节点的方法
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        queue = [root]
        vals = []
        while queue:
            cur = queue.pop(0)
            if cur is None:
                continue
            vals.append(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)

        vals.sort(key=lambda x: abs(target-x))
        return vals[: k]

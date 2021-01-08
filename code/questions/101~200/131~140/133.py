"""
https://leetcode-cn.com/problems/clone-graph
"""

# Definition for a Node.


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return 'node[{0}]'.format(self.val)


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        old2new = {}
        queue = [node]
        while queue:
            cur = queue.pop(0)
            old2new[cur] = Node(cur.val)
            for neighbor in cur.neighbors:
                if neighbor in old2new:
                    continue
                queue.append(neighbor)

        for old, new in old2new.items():
            new.neighbors = [old2new[old_neighbor] for old_neighbor in old.neighbors]
        return old2new[node]


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    Solution().cloneGraph(node1)


if __name__ == '__main__':
    main()

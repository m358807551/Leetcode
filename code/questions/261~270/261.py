"""
https://leetcode-cn.com/problems/graph-valid-tree/
"""
from collections import defaultdict


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(dict)
        for a, b in edges:
            adj[a][b] = adj[b][a] = 1

        queue, visited = [0], set()
        while queue:
            cur = queue.pop(0)
            if cur in visited:
                return False
            visited.add(cur)
            for next_ in list(adj[cur].keys()):
                queue.append(next_)
                adj[cur].pop(next_, None)
                adj[next_].pop(cur, None)

        return len(visited) == n


print(
    Solution().validTree(
        n=5,
edges = [[0,1], [0,2], [0,3], [1, 4]]
    )
)

"""
https://leetcode-cn.com/problems/walls-and-gates/
"""
"""
给定二维网格：

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
运行完你的函数后，该网格应该变成：

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
from pprint import pprint

inf = 2147483647


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        self.rooms = rooms
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.bfs(i, j, 0)

    def bfs(self, i, j, distance):
        self.rooms[i][j] = distance
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i+x < len(self.rooms) and 0 <= j+y < len(self.rooms[0]) and distance + 1 < self.rooms[i+x][j+y]:
                self.bfs(i+x, j+y, distance+1)

pprint(
    Solution().wallsAndGates(
        [
            [inf, -1, 0, inf],
            [inf, inf, inf, -1],
            [inf, -1, inf, -1],
            [0, -1, inf, inf]]
    )
)

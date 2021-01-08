"""
https://leetcode-cn.com/problems/best-meeting-point/
"""
from pprint import pprint

INF = float('inf')


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        points = [
            (i, j)
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j]
        ]
        x_list, y_list = sorted(p[0] for p in points), sorted(p[1] for p in points)
        r, c = x_list[len(x_list) // 2], y_list[len(y_list) // 2]

        return sum(abs(r-x)+abs(y-c) for x, y in points)

pprint(
    Solution().minTotalDistance(
        [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    )
)

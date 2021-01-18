"""
https://leetcode-cn.com/problems/number-of-islands
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        grid = [list(line) for line in grid]
        k = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs(grid, i, j, k):
                    k += 1
        return k-1

    def dfs(self, grid, i, j, k):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == '1':
                grid[i][j] = k
                self.dfs(grid, i-1, j, k)
                self.dfs(grid, i+1, j, k)
                self.dfs(grid, i, j-1, k)
                self.dfs(grid, i, j+1, k)
                return True


print(
    Solution().numIslands(
        [
'11000',
'11000',
'00100',
'00011',
        ]
    )
)
